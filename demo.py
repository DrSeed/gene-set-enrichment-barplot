import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(5)
sets=["Cell cycle","Immune response","Apoptosis","Oxidative phosphorylation","DNA repair","Inflammation","Cytokine signalling","Metabolism"]
p=np.sort(rng.uniform(1e-8,0.2,len(sets))); score=-np.log10(p)
plt.figure(figsize=(7,4)); y=np.arange(len(sets))
plt.barh(y,score,color=plt.cm.viridis(score/score.max()))
plt.yticks(y,sets); plt.gca().invert_yaxis(); plt.xlabel("-log10(adjusted p)")
plt.title("Pathway enrichment (demo data)")
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("top pathway: "+sets[int(np.argmax(score))]+"\n"); print("ok")