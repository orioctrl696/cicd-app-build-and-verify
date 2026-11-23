# 🚀 SpringBoot CI/CD Pipeline

**Auto-triggered quality gates for Spring Boot applications**

---

## 📋 What This Does

```
GitHub Push/PR/Merge → 🔔 Auto Trigger → 7 Quality Gates → 💾 Save JAR → ✅ Ready to Publish
```

**Pipeline automatically runs:**
- ✅ Code quality checks (Lint)
- ✅ Security scans (Secret Scan, Coverity, Black Duck*)
- ✅ Build & test your Spring Boot app
- ✅ Saves JAR artifact for publish pipeline
- ✅ Creates build metadata for traceability

**Runtime:** ~10 minutes (Push) | ~15 minutes (PR)* | **Platform:** Harness Cloud

<sub>* Black Duck SCA runs only on Pull Requests (saves 5 minutes on regular pushes)</sub>

---

## 🎯 7 Pipeline Steps

| Step | What It Does | Time | When Runs |
|------|-------------|------|-----------|
| 1️⃣ **Lint** | Code quality check | 30s | Always |
| 2️⃣ **Secret Scan** | Detects exposed credentials | 45s | Always |
| 3️⃣ **Dependencies** | Downloads from JFrog | 2m | Always |
| 4️⃣ **Build** | Creates JAR + Saves to /harness/outputs/ | 1.5m | Always |
| 5️⃣ **Unit Tests** | Runs JUnit tests | 45s | Always |
| 6️⃣ **Coverity SAST** | Security vulnerability scan | 5m | Always |
| 7️⃣ **Black Duck SCA** | Dependency vulnerability scan (PR only) | 5m | **PRs Only** ⚡ |

**Note:** Black Duck only runs on Pull Requests, saving ~5 minutes on regular pushes!

---

## 🔀 Branch Configuration

### **Current Setup:**
```yaml
build: <+input>
```

### **What This Means:**

| Scenario | What Happens |
|----------|-------------|
| **Push to GitHub** | Automatically uses pushed branch ✅ |
| **Create PR** | Automatically uses PR source branch ✅ |
| **Manual Run** | Allows branch selection ✅ |

---

## 💾 JAR Artifact & Pipeline Integration

### **Build Output:**

The Build step (Step 4) automatically saves the JAR artifact for downstream pipelines:

```bash
# What happens in Build step:
1. mvn clean package -DskipTests -B          # Creates JAR
2. cp target/*.jar /harness/outputs/demo.jar # Saves to shared location
3. Creates build-info.json                    # Metadata for traceability
```

**Artifact Location:** `/harness/outputs/demo.jar`

**Metadata Created:** `/harness/outputs/build-info.json`
```json
{
  "jarFile": "demo.jar",
  "jarPath": "/harness/outputs/demo.jar",
  "buildId": "<pipeline.sequenceId>",
  "pipelineId": "<pipeline.executionId>",
  "commitSha": "<trigger.commitSha>",
  "branch": "<trigger.branch>",
  "timestamp": "2026-11-20T10:15:30Z"
}
```

### **Integration with Publish Pipeline:**

This pipeline works seamlessly with **cicd-app-package-and-publish**:

```
Build Pipeline (THIS)          Publish Pipeline
      ↓                              ↓
Builds JAR file        →       Retrieves JAR from
Saves to /harness/     →       /harness/outputs/
Creates metadata       →       Publishes to JFrog
```

**Benefits:**
- ✅ **Automatic artifact passing** - No manual file transfers
- ✅ **Full traceability** - Build ID, commit SHA, branch tracked
- ✅ **Parallel workflows** - Build once, publish to multiple environments
- ✅ **Clean separation** - Build/verify separate from package/publish

**Related Pipeline:** [cicd-app-package-and-publish](../cicd-app-package-and-publish/)

---

## 🚀 Quick Setup (4 Steps)

### **1. Create GitHub Connectors**

In Harness → Connectors → New Connector:

```yaml
# Connector 1: App Repository
Name: github_app_connector
URL: https://github.aepsc.com
Auth: Personal Access Token

# Connector 2: DevOps Scripts
Name: github_devops_connector
URL: https://github.aepsc.com
Auth: Personal Access Token
```

---

### **2. Add Secrets**

In Harness → Secrets:

| Secret Name | Description |
|-------------|-------------|
| `github_app_token` | App repo access token |
| `github_devops_token` | DevOps repo access token |
| `jfrog_username` | JFrog username |
| `jfrog_password` | JFrog API token |

---

### **3. Import Pipeline**

```
Harness → Pipelines → Create Pipeline → Import from YAML
Select: app-build-verify.yaml
Click: Save
```

**✅ Pipeline + Trigger both imported automatically!**

---

### **4. Configure Webhook**

In GitHub Repo → Settings → Webhooks:

```
Payload URL: [Copy from Harness trigger]
Content type: application/json
Events: ☑ Pushes, ☑ Pull requests
Active: ☑
```

---

## 🧪 Test Your Pipeline

```bash
# Test 1: Push
git checkout -b feature/test
git push origin feature/test
# ✅ Pipeline auto-starts

# Test 2: Manual run with different branch
Harness → Run Pipeline → Enter branch name
# ✅ Override default branch
```

---

## 📦 How DevOps Scripts Work

**Pipeline auto-clones two repositories:**

```
1. Your App Code (main repo)
   ↓
2. DevOps Scripts (from DevOps/devops-automation)
   ↓
Both available in: /harness/workspace/
   ↓
Scripts used: lint.py, secret_scan.py, coverity.py, blackduck.py
```

**No manual downloads needed!** Scripts are automatically cloned and ready to use.

---

## 🐛 Common Issues

### ❌ Pipeline not triggering
```
✓ Check webhook is configured in GitHub
✓ Verify webhook shows successful deliveries
✓ Ensure trigger is enabled in Harness
```

### ❌ Pipeline waits for input
```
Problem: Using build: <+input> (blocks automation, always waits)
Solution: Change to build: <+input>.default(<+trigger.branch>)
Benefit: Automatic triggers work seamlessly, manual runs still possible
```

### ❌ Dependencies fail
```
✓ Verify JFrog credentials in Harness Secrets
✓ Check Maven settings.xml configuration
```

### ❌ Scripts not found
```
Error: python3: can't open file 'devops-automation/scripts/lint.py'

✓ Verify github_devops_connector has correct token
✓ Check token has access to DevOps/devops-automation repo
```

---

## ❓ FAQ

**Q: Why `.default()` in build configuration?**  
**A:** Supports both automatic (90%) and manual (10%) execution. Best practice for production CI/CD.

**Q: Can I test a different branch manually?**  
**A:** Yes! Harness → Run Pipeline → Enter custom branch name → Run

**Q: What branch does automatic trigger use?**  
**A:** 
- Push → Uses pushed branch
- PR → Uses source branch  
- Merge → Uses target branch

**Q: How do I know which event triggered the pipeline?**  
**A:** Check variable `triggerType` = `<+trigger.event>` (shows: push, pull_request, etc.)

**Q: Why does Black Duck only run on PRs?**  
**A:** 
- Saves ~5 minutes on regular pushes (faster feedback for developers)
- PRs are the quality gate before merging to main
- Full security scan where it matters most
- Configured via: `when.condition: <+pipeline.variables.triggerType> == "pull_request"`

**Q: Where is the JAR artifact saved?**  
**A:** 
- **Location:** `/harness/outputs/demo.jar`
- **Metadata:** `/harness/outputs/build-info.json`
- **Available to:** cicd-app-package-and-publish pipeline
- **Contains:** Build ID, commit SHA, branch, timestamp

**Q: How does the publish pipeline get the JAR?**  
**A:** Harness shared paths (`/harness/outputs/`) automatically make artifacts available to downstream pipelines. The publish pipeline reads from this location.

**Q: What if I want Black Duck on every run?**  
**A:** Remove the `when` condition from Step 7 in [app-build-verify.yaml](app-build-verify.yaml) (lines 245-247). Note: This adds ~5 minutes to every push.

---

## ✅ Best Practices

```yaml
✓ Use: <+input>.default(<+trigger.branch>)  # Smart defaults: Auto-run + Manual override
✓ Store all credentials in Harness Secrets   # Never commit secrets to Git
✓ Use additionalRepositories for scripts     # Centralized, reusable DevOps scripts
✓ Single auto-trigger (not 3 separate)       # Simpler maintenance, cleaner config
✓ Set up email notifications                 # Monitor pipeline health and failures
```

---

## 🎯 Pipeline Flow Diagram

```
Developer Pushes Code
    ↓
GitHub Webhook Triggered
    ↓
Harness Pipeline Starts
    ↓
┌───────────────────────────────────────┐
│  Clone Repositories                   │ ← App code + DevOps scripts
├───────────────────────────────────────┤
│  1. Lint                             │ ← Code quality
│  2. Secret Scan                      │ ← Security
│  3. Dependencies                     │ ← Maven + JFrog
│  4. Build                            │ ← Create JAR
│     └─ Save to /harness/outputs/    │ ← Artifact saving
│     └─ Create build-info.json       │ ← Metadata
│  5. Unit Tests                       │ ← JUnit
│  6. Coverity SAST                    │ ← Vulnerability scan
│  7. Black Duck SCA (PRs only)        │ ← Component scan*
└───────────────────────────────────────┘
    ↓
✅ JAR Saved at /harness/outputs/demo.jar
    ↓
Ready for cicd-app-package-and-publish pipeline

* Black Duck only runs on Pull Requests
```

---

## 📊 Pipeline Variables

| Variable | Value | Usage |
|----------|-------|-------|
| `triggerType` | `<+trigger.event>` | Event type (push/pr/merge) |
| `<+trigger.branch>` | Branch name | Auto-detected from GitHub |
| `<+project.identifier>` | Project ID | Project context |
| `<+org.identifier>` | Org ID | Organization context |

---

## 🎓 Key Takeaways

1. **Fully Automated** - Push code, pipeline runs automatically
2. **7 Quality Gates** - Code quality + Security + Testing
3. **Smart Configuration** - Auto-execution with manual override option
4. **Centralized Scripts** - DevOps scripts auto-cloned from shared repo
5. **Conditional Execution** - Black Duck only on PRs (saves 5 min on pushes)
6. **Artifact Pipeline** - JAR saved to /harness/outputs/ for publish pipeline
7. **Full Traceability** - Build metadata tracks: commit SHA, branch, build ID
8. **Zero Manual Steps** - Webhook → Build → Save JAR → Test → Scan 

---

## 📚 Related Files

**Pipeline Files:**
- [app-build-verify.yaml](app-build-verify.yaml) - Main pipeline configuration
- [cicd-app-package-and-publish](../cicd-app-package-and-publish/) - Downstream publish pipeline

**Demo Materials:**
- [PIPELINE-DEMO-GUIDE.md](PIPELINE-DEMO-GUIDE.md) - Complete presentation guide
- [DEMO-CHEAT-SHEET.md](DEMO-CHEAT-SHEET.md) - Quick reference for demos
- [DEMO-VISUALS.md](DEMO-VISUALS.md) - Visual diagrams and flowcharts

---

## 🎉 Summary

**This pipeline provides:**
- ✅ Complete CI/CD automation (webhook → artifact)
- ✅ 7-layer quality and security validation
- ✅ Smart execution (conditional Black Duck on PRs)
- ✅ Artifact management (JAR + metadata saved)
- ✅ Full traceability (build ID → commit SHA → source)
- ✅ Integration ready (works with publish pipeline)

**Perfect for:** Enterprise Spring Boot applications requiring security compliance and quality gates

---

**🚀 Ready to build with confidence!**

