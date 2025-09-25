

## MediaPipe Hand Landmarks (21 points)

| Index | Finger / Joint | Notes |
|-------|----------------|-------|
| **0** | Wrist | Base reference point |
| **1** | Thumb CMC | Base of thumb (carpometacarpal) |
| **2** | Thumb MCP | Thumb knuckle (metacarpophalangeal) |
| **3** | Thumb IP | Thumb middle joint (interphalangeal) |
| **4** | Thumb Tip | End of thumb |
| **5** | Index MCP | Index knuckle |
| **6** | Index PIP | Index middle joint |
| **7** | Index DIP | Index near-tip joint |
| **8** | Index Tip | End of index finger |
| **9** | Middle MCP | Middle finger knuckle |
| **10** | Middle PIP | Middle finger middle joint |
| **11** | Middle DIP | Middle finger near-tip joint |
| **12** | Middle Tip | End of middle finger |
| **13** | Ring MCP | Ring finger knuckle |
| **14** | Ring PIP | Ring finger middle joint |
| **15** | Ring DIP | Ring finger near-tip joint |
| **16** | Ring Tip | End of ring finger |
| **17** | Pinky MCP | Pinky knuckle |
| **18** | Pinky PIP | Pinky middle joint |
| **19** | Pinky DIP | Pinky near-tip joint |
| **20** | Pinky Tip | End of pinky |

---

## The usage method

- **Index, Middle, Ring, Pinky**:  
  Compare **tip (8, 12, 16, 20)** with **PIP joint (6, 10, 14, 18)**.  
  - If tip.y < pip.y → finger is extended (tip higher up).  
  - If tip.y > pip.y → finger is folded.

- **Thumb**:  
  Compare **tip (4)** with **joint (3)** on the **x-axis**.  
  - On the right hand: if tip.x < joint.x → thumb extended.  
  - On the left hand: if tip.x > joint.x → thumb extended.  

---

## Logic
The gesture logic:
- Open Palm → all tips above their joints.  
- Fist → all tips below their joints.  
- Peace Sign → index + middle extended, others folded.  
- Thumbs Up → thumb extended sideways, others folded.  

---

*“I checked whether the finger was open or closed by using landmarks 8 vs 6 for the index finger, 12 vs 10 for the middle finger”*

---
