# Module 7 — Regulated & Disconnected Deployment

**Time:** ~4 hours · **You'll be able to:** map compliance requirements to architectural choices, explain software supply-chain security, and use lessons from air-gapped environments in any regulated enterprise.

[← Module 6](06-evals.md) · [Course home](README.md) · [Next: Module 8 →](08-discovery-and-diagnosis.md)

---

## The big idea

The hardest FDE environments (classified enclaves, ships, factory floors) have no internet and no shortcuts. You probably won't deploy to a submarine, but **every regulated enterprise is partly air-gapped**: restricted egress, approved-software lists, change-control boards, data that can't leave a region, auditors who ask "prove it." The air-gap playbook is the most extreme version of what your organization's security, risk, and compliance teams need, and engineers who think this way get approvals faster.

**Core principle:** in regulated environments, *compliance requirements are architecture requirements*. Learn them on the discovery call, not in week 12.

---

## Learn

### 1. The compliance bedrock, translated

The roadmap's defense/government terms each have an equivalent in a typical regulated enterprise. Learn the pattern, then find your organization's local version.

| Roadmap term (defense/gov) | What it really is | Typical enterprise equivalent |
| :--- | :--- | :--- |
| **ATO** (Authority to Operate), via NIST RMF | A formal sign-off that a system's risks are accepted before it runs in production | Architecture/security review board, production readiness review, model or AI governance approval |
| **Impact Levels / FedRAMP** | Tiers of data sensitivity that restrict which platforms you may use | Internal data classification (public / internal / confidential / restricted) and approved-vendor lists |
| **STIGs** | Line-by-line hardening checklists | CIS Benchmarks, internal hardening baselines, golden images |
| **ITAR / EAR** | Legal limits on where controlled data (even model weights) may go | Data residency, cross-border transfer rules (e.g., GDPR), client contractual restrictions |
| **CMMC / NIST 800-171** | Contractor security certification | SOC 2, ISO 27001, vendor risk assessments |
| **Cross-Domain Solutions, data diodes** | Strictly controlled movement of data between trust levels | Egress controls, DLP, approved file-transfer paths, perimeters (VPC SC) |

Sector-specific regimes add their own layer. Healthcare has HIPAA. In financial services, model risk management guidance (in US banking, the Federal Reserve/OCC's SR 11-7) shapes how models, increasingly including AI systems, must be validated, documented, and monitored. Find out which apply to your organization and who interprets them internally.

### 2. Software supply chain: "where did this come from?"

Air-gapped sites can't `pip install`, so everything is pre-staged, verified, and recorded. The same discipline is becoming standard everywhere:

- **Package mirrors:** internal PyPI/npm/APT mirrors (`devpi`, `Verdaccio`, `apt-mirror`, or Artifactory/Nexus); nothing installs from the public internet.
- **CVE scanning:** every artifact passes through **Trivy** or **Grype** before approval.
- **Hardened images:** minimal bases (`distroless`, Chainguard) or approved catalogs (the DoD's **Iron Bank**). A container with no shell gives an attacker less to work with.
- **Signing & admission control:** sign images with **Cosign** (Sigstore); **Kyverno** or **OPA Gatekeeper** rejects unsigned images at deploy time.
- **Private registries:** **Harbor** with replication, signing, and scanning.

### 3. Models are artifacts too

- Load weights with **`safetensors`**, not pickle. Pickle files can execute code when loaded.
- Keep **provenance** for every model: source, license (Apache 2.0? Llama Community? Gemma Terms?), checksums, training-data attestation. "We downloaded it from Hugging Face" won't satisfy an auditor.
- **Local inference runtimes** (vLLM, Ollama, llama.cpp, TensorRT-LLM) run open-weight models when data can't leave the environment. Even if your organization uses hosted models today, know this option for the most sensitive data.
- **Hosted model questions to ask:** Where is data processed? Is it retained or used for training? Which regions? What certifications does the provider hold? Is it on your organization's approved list?

### 4. Failure modes that never happen in a demo

From the roadmap's air-gap list, and they apply to locked-down corporate networks too:
- **Clock drift** → TLS and Kerberos failures. (Corporate equivalent: proxies and TLS-inspection breaking SDKs.)
- **Certificate rotation** → you need an internal PKI story. (Corporate: who issues internal certs, and how often do they expire?)
- **Secrets management** → Vault, HSMs, SOPS. Never secrets in code or notebooks.
- **The "first boot" problem** → how does configuration get into a locked environment? Corporate equivalent: change-control windows, so plan releases around them.
- **Store-and-forward telemetry** → design logging that survives network gaps (Fluent Bit + local buffer).

---

## Lab — Control map for a sensitive deployment (90 min)

**Scenario:** deploy the Module 4 policy assistant for a team that handles **confidential client data**. Data must stay in one region; the model provider must not retain prompts; every answer must be auditable.

Build a **control map**, a table with one row per requirement:

| Requirement | Source (policy/regulation) | Architectural control | Evidence an auditor would accept | Owner |
| :--- | :--- | :--- | :--- | :--- |
| Data stays in region X | Data-residency policy | Regional resources only; org policy constraint on locations | IaC + org-policy config export | Platform team |
| No prompt retention by provider | Vendor risk standard | Enterprise agreement with zero retention; private endpoint | Contract clause + vendor attestation | Procurement / Security |
| Every answer auditable | AI governance | Log question, retrieved doc IDs, answer, model version | Sample audit log + retention setting | FDE / Run team |
| … | | | | |

Add at least six more rows covering: access control on documents, secrets, image provenance, vulnerability scanning, change management, and model/version change approval.

Stretch: run `trivy image python:3.12` and then `trivy image gcr.io/distroless/python3`. Compare the CVE counts and explain the difference in one sentence.

---

## Articulate

**Drill 7.1 — For a risk/compliance partner (60 seconds).** Walk through your control map: *"For each requirement, here's the control and here's the evidence you'll get."* Compliance teams respond well to engineers who arrive with evidence already planned.

**Drill 7.2 — For an exec (30 seconds):**
> *"Compliance isn't a gate at the end. We built the controls into the design: data stays in-region, the vendor doesn't keep our data, and every answer is logged and traceable. That's why the review takes weeks, not quarters."*

**Drill 7.3 — Push-back answers:**
- *"Security will never approve this."* → "What specifically would they object to? Let's ask them now and design for it." Bring them in at discovery.
- *"Can't we just use the public API for the pilot?"* → Pilots with real data are production from a compliance perspective. Use synthetic or approved data, or the approved endpoint.

---

## Drive it at work

- [ ] Find your organization's data classification scheme and classify your mission's data.
- [ ] List the approvals your mission needs to reach production (security review, architecture board, AI/model governance, privacy, vendor risk) and the **lead time** of each. Put the longest one on your critical path now.
- [ ] Build the control map for your mission and put it in **Section 7** of your field notebook.
- [ ] Meet one person from security or risk *before* you need their approval. Ask: *"What do teams usually get wrong when they bring you AI projects?"*

---

## Check yourself

<details><summary>1. Why load model weights with safetensors rather than pickle?</summary>
Pickle can execute arbitrary code when loaded; safetensors is a pure data format.
</details>

<details><summary>2. What does image signing + admission control give you?</summary>
A guarantee that only images built and approved by your trusted pipeline can run. Tampered or unknown images are rejected at deploy time.
</details>

<details><summary>3. What's the enterprise equivalent of an ATO, and why does it belong on day 1?</summary>
The production approval process (security/architecture/AI-governance reviews). It has long lead times and specific evidence requirements that shape the architecture, so discovering them late causes rework and delays.
</details>

<details><summary>4. Name four questions to ask about a hosted model provider.</summary>
Data processing location/region, retention and training use of prompts, certifications (SOC 2, ISO 27001, etc.), private connectivity options, and whether it's on the approved vendor list.
</details>

---

## Go deeper

- [DoD Platform One](https://p1.dso.mil/) and the [DoD Enterprise DevSecOps Reference Design](https://public.cyber.mil/devsecops/): the patterns transfer to any regulated enterprise
- [NIST Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
- [Sigstore](https://www.sigstore.dev/) · [Trivy](https://github.com/aquasecurity/trivy) · [Harbor](https://goharbor.io/) · [Kyverno](https://kyverno.io/)
- [K3s air-gap install guide](https://docs.k3s.io/installation/airgap): a concrete walkthrough
- [Import AI](https://jack-clark.net/): AI policy alongside progress
- Roadmap: [Air-Gapped & Tactical Edge Deployment](../README.md#-air-gapped--tactical-edge-deployment)

[Next: Module 8 — Discovery & Diagnosis →](08-discovery-and-diagnosis.md)
