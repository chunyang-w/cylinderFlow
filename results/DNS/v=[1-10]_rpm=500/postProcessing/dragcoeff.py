# %% import and set up
import os
import pandas as pd
import matplotlib.pyplot as plt

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, "forceCoeffsIncompressible/0/forceCoeffs.dat") # noqa

# %% Reading the data
time_end = 5
v_init = 1
v_end = 10
slope_v = (v_end - v_init) / time_end

df = pd.read_csv(
    file_path,
    delim_whitespace=True,
    comment="#",
    header=None,
    names=["t", "cm", "cd", "cl", "cl(f)", "cl(r)"]
)

df["v"] = 1 + df["t"] * slope_v

# df.tail()

# %% Plotting the drag coefficient
stride = 1500
v = df["v"][::stride]
cd = df["cd"][::stride]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(v, cd, "o-", label="$C_d$", color="b")
ax.legend()
ax.grid(alpha=0.5)
ax.set_xlabel("Velocity [m/s]")
ax.set_ylabel("Drag coefficient")



# %% save plot
fig.savefig("dragcoeff.png", dpi=500, bbox_inches="tight")

# %%
