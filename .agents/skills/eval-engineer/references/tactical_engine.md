# LLM Evaluation Tactical Engine

## 📊 Evaluation Workflow
2. **Golden Dataset**: Compile input -> ground truth pairs, including adversarial edge cases.
3. **Evaluation Harness**: Use a stronger "Judge Model" (e.g., GPT-4o) with a strict `<reasoning>` block rubric.
4. **CI/CD Integration**: Block merges if prompt evaluation scores drop below threshold.

## ⚠️ Detailed Troubleshooting
| Symptom | Root Cause | Fix / Recovery |
| Markdown instead of JSON | Weak constraints | Enforce "JSON Mode" and provide strict Zod schema. |
| Judge gives 5/5 to bad output | Vague rubric | Add negative examples to Judge instructions; mandate reasoning. |
| "Works on my machine" failure | Over-fitting data | Expand Golden Dataset with chaotic and out-of-domain queries. |

---
*Preserved from Portable Brainvibing Infrastructure*