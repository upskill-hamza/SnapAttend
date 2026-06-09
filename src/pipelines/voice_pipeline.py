from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io 
import librosa
import streamlit as st


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    
    except Exception as e:
        st.error('Voice enrollment failed')
        return None


def identify_speaker(new_embedding, candidates_dict, threshold = 0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0
    
    best_sid = None
    best_score = -1.0
    
    new_emb_np = np.array(new_embedding)
    
    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding:
            stored_emb_np = np.array(stored_embedding)
            
            dot_product = np.dot(new_emb_np, stored_emb_np)
            norm_new = np.linalg.norm(new_emb_np)
            norm_stored = np.linalg.norm(stored_emb_np)
            
            similarity = dot_product / (norm_new * norm_stored)
            
            if similarity > best_score:
                best_score = similarity
                best_sid = sid
            
    
    if best_score >= threshold:
        return best_sid, float(best_score)
    
    return None, float(best_score)


def process_bulk_audio(audio_bytes, candidates_dict, threshold = 0.65):
    
    try:
        encoder = load_voice_encoder()
        
        try:
            audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        except Exception as audio_err:
            st.error(f"Audio file decoding error. Verify the encoding format: {audio_err}")
            return {}

        segments = librosa.effects.split(audio, top_db=30)
        identified_results = {}
        
        normalized_candidates = {}
        for sid, stored_emb in candidates_dict.items():
            if stored_emb:
                arr = np.array(stored_emb)
                norm = np.linalg.norm(arr)
                if norm > 0:
                    normalized_candidates[sid] = (arr / norm)

        if not normalized_candidates:
            return {}

        for start, end in segments:
            
            if (end - start) < sr * 0.5:
                continue
                
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            
            embedding = encoder.embed_utterance(wav)
            norm_new = np.linalg.norm(embedding)
            if norm_new == 0:
                continue
            new_emb_unit = embedding / norm_new
            
            best_sid = None
            best_score = -1.0
            
            for sid, stored_emb_unit in normalized_candidates.items():
                
                similarity = np.dot(new_emb_unit, stored_emb_unit)
                if similarity > best_score:
                    best_score = float(similarity)
                    best_sid = sid
                    
            if best_sid and best_score >= threshold:
                if best_sid not in identified_results or best_score > identified_results[best_sid]:
                    identified_results[best_sid] = best_score
                
        return identified_results
    except Exception as e:
        st.error(f"Bulk process error: {e}")
        