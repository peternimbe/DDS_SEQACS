import numpy as np, pandas as pd
from pathlib import Path

def load_seqacs(data_dir):
    files=sorted(Path(data_dir).glob("seqacs_part_*.csv"))
    if not files: raise FileNotFoundError("No seqacs_part_*.csv files found.")
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

def validate_schema(df):
    required={"scenario","qber","qkd_information_leakage","pqc_adversarial_advantage",
              "threat_score","ddsr_qkd_only","ddsr_pqc_only","ddsr_static_hybrid",
              "ddsr_seqacs","seqacs_action","adaptation_time_sec","availability_score",
              "resilience_score","attack_present","attack_detected"}
    missing=required-set(df.columns)
    if missing: raise ValueError(f"Missing required columns: {sorted(missing)}")
    return True

def theorem_product(lq,lc): return np.asarray(lq,float)*np.asarray(lc,float)
def weak_dominance(lq,lc): 
    h=theorem_product(lq,lc); return h<=np.minimum(lq,lc)+1e-15

def adv_qkd(lam,a=1.): return np.exp2(-a*np.asarray(lam,float))
def adv_pqc(lam,b=1.): return np.exp2(-b*np.asarray(lam,float))
def adv_dds(lam,a=1.,b=1.): return np.exp2(-(a+b)*np.asarray(lam,float))

def scenario_summary(df):
    cols=["qber","qkd_information_leakage","pqc_adversarial_advantage","threat_score",
          "ddsr_qkd_only","ddsr_pqc_only","ddsr_static_hybrid","ddsr_seqacs",
          "adaptation_time_sec","availability_score","resilience_score"]
    return df.groupby("scenario")[cols].agg(["mean","std","median","count"])

def detection_rate(df):
    attacked=df[df.attack_present==1]
    return attacked.attack_detected.mean() if len(attacked) else np.nan
