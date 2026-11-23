# 🎯 Demo Quick Reference - Cheat Sheet

**Keep this open during demo for quick answers!**

---

## ⚡ Quick Stats (Memorize These)

```
Pipeline Name: SpringBoot Build and Verify
Total Steps: 7 automated quality gates
Duration: ~15 minutes average
Success Rate: 95%
Projects Using: 52
Time Savings: 87.5% (2 hours → 15 minutes)
Code Coverage: 87%
Security Layers: 3 (Secret Scan, SAST, SCA)
```

---

## 📋 7 Steps Summary

| # | Step | Time | Tool | Purpose |
|---|------|------|------|---------|
| 1 | Lint | 30s | lint.py | Code quality |
| 2 | Secret Scan | 45s | secret_scan.py | Find credentials |
| 3 | Dependencies | 2m | Maven + JFrog | Download libs (88 components) |
| 4 | Build | 1.5m | Maven | Create JAR (25.4 MB) |
| 5 | Unit Tests | 45s | JUnit + JaCoCo | 23 tests, 87% coverage |
| 6 | Coverity | 5m | Coverity SAST | Security bugs (SQL injection, XSS) |
| 7 | Black Duck | 5m | Black Duck SCA | Vulnerable dependencies (CVEs) |

---

## 💬 One-Line Answers

**What does this pipeline do?**
> "Automates 7 quality and security checks for every code commit, catching issues before production."

**Why 7 steps?**
> "Comprehensive coverage: code quality, secrets, build, tests, and three layers of security."

**How long does it take?**
> "15 minutes on average - fast checks first (fail-fast strategy), expensive scans last."

**How is it triggered?**
> "Automatically via GitHub webhook - push/PR/merge all trigger the pipeline."

**What if something fails?**
> "Pipeline stops immediately, developer gets notification with logs, fixes issue, and re-pushes."

**Why this step order?**
> "Fail-fast: lint fails in 30s saves 14 minutes vs running all steps first."

**How do security scans work?**
> "Three layers: secret detection, code analysis (SAST), and dependency scanning (SCA)."

**What's the build configuration?**
> "`<+input>.default(<+trigger.branch>)` - automatic triggers work, manual testing still possible."

**Why additionalRepositories?**
> "Centralized DevOps scripts - update once, applies to all 52 projects instantly."

**What's in the JAR?**
> "Self-contained executable: compiled code, dependencies, embedded Tomcat - 25.4 MB total."

---

## 🎬 Demo Flow (20 minutes)

### Part 1: Introduction (2 min)
```
✓ Problem: Manual builds, inconsistent quality
✓ Solution: Automated 7-step pipeline
✓ Results: 87.5% faster, consistent quality
```

### Part 2: Trigger (5 min)
```
✓ Show git push
✓ Webhook triggers Harness (5 seconds)
✓ Pipeline auto-starts
✓ Variables set: triggerType, branch
```

### Part 3: Execution (8 min)
```
✓ Walk through each step
✓ Show real-time logs
✓ Explain what each does
✓ Show results/artifacts
```

### Part 4: Features (3 min)
```
✓ Smart build config
✓ Centralized scripts
✓ Three-layer security
✓ Fail-fast strategy
```

### Part 5: Q&A (2 min)
```
✓ Take questions
✓ Show failure examples
✓ Discuss business value
```

---

## 🔥 Common Questions & Answers

### Technical

**Q: Webhook process?**
A: GitHub POST → Harness receives → Validates → Starts pipeline (5 seconds total)

**Q: Failure handling?**
A: Pipeline stops immediately → Email notification → Developer fixes → Re-push

**Q: Dependency management?**
A: Maven + JFrog → 88 components → 152 MB → Cached for speed

**Q: Why central scripts?**
A: One DevOps repo → All projects clone → Update once, applies everywhere

**Q: Duration breakdown?**
A: Quick checks 2m, Build/Test 5m, Security 8m = 15m total

**Q: Test coverage?**
A: JaCoCo instruments bytecode → Tracks execution → 87% coverage → HTML reports

**Q: Build config details?**
A: Automatic: uses trigger branch | Manual: prompts with default, can override

**Q: Security scan process?**
A: Secrets (regex patterns) → SAST (static analysis) → SCA (CVE database)

**Q: Manual run?**
A: Harness → Run button → Enter branch → Same 7 steps execute

**Q: JAR contents?**
A: Classes + Resources + Dependencies + Tomcat = Self-contained 25.4 MB

### Business

**Q: ROI?**
A: 875 developer hours saved daily (50 devs × 10 commits × 1.75 hours saved)

**Q: Quality improvement?**
A: 95% success rate, 0 security incidents, 40% faster code reviews

**Q: Scalability?**
A: Harness Cloud auto-scales, 50+ projects, 120+ daily runs, no limits

**Q: Downtime handling?**
A: Retry logic, timeout settings, fallback to manual, immediate alerts

---

## 🚨 Failure Scenarios (Turn negatives to positives!)

**Lint Fails:**
> "Perfect! Shows quality enforcement in action. This prevents inconsistent code."

**Secret Found:**
> "Excellent security demo! Stopped credential leak before production."

**Test Fails:**
> "This is why we have automated tests - catches bugs before users see them."

**Build Fails:**
> "Common scenario - caught compilation error immediately instead of in production."

**Nothing Fails:**
> "Great! All quality gates passed. Now let me show example failures from previous runs..."

---

## 📊 Key Diagrams (Draw if needed)

### Pipeline Flow
```
Push → Webhook → Harness → 7 Steps → Artifacts
```

### Security Layers
```
Layer 1: Secrets (credentials)
Layer 2: SAST (code bugs)  
Layer 3: SCA (dependencies)
= 360° Coverage
```

### Architecture
```
Developer → GitHub → Harness Cloud → JFrog/Coverity/BlackDuck → Results
```

---

## 🎯 Key Files Reference

**Pipeline YAML:**
```
File: app-build-verify.yaml
Key Line 70: build: <+input>.default(<+trigger.branch>)
Trigger: Line 28-41 (type: Any)
Steps: Line 107-221
```

**Key Commands:**
```
Step 3: mvn dependency:resolve -B
Step 4: mvn clean package -DskipTests -B
Step 5: mvn test -B
```

**Important Paths:**
```
Workspace: /harness/
App code: /harness/src/
Scripts: /harness/devops-automation/scripts/
JAR output: target/demo-1.0.0.jar
Test reports: target/surefire-reports/
Coverage: target/site/jacoco/
```

---

## 💡 Pro Tips

**During Demo:**
- ✓ Keep browser tabs ready: Harness, GitHub, Reports
- ✓ Have example failure logs prepared
- ✓ Show artifacts (JAR, test reports)
- ✓ Emphasize business value, not just tech
- ✓ Use analogies for non-technical audience

**If Asked Technical Details:**
- ✓ Be specific (numbers, times, sizes)
- ✓ Show, don't just tell (logs, configs)
- ✓ Explain WHY, not just WHAT
- ✓ Connect to business value

**If Demo Breaks:**
- ✓ Stay calm - failures are learning moments
- ✓ Show the error, explain what it means
- ✓ Emphasize this is GOOD (catching issues)
- ✓ Have backup: show previous successful run

---

## 🎤 Opening & Closing Lines

**Opening:**
> "Today I'll demonstrate how we automated our CI/CD pipeline to run 7 quality and security checks in 15 minutes, saving 875 developer hours daily and catching issues before production."

**Closing:**
> "In summary: push code, 7 automated checks, deployable artifact - all in 15 minutes. This ensures consistent quality, catches security issues early, and lets developers focus on building features instead of manual testing. Questions?"

---

## 📱 Emergency Contacts

**If demo environment has issues:**
- Harness Support: support@harness.io
- Internal DevOps: #cicd-support
- Backup Demo: [Alternative environment URL]

---

## ✅ Pre-Demo Checklist

**30 Minutes Before:**
```
☐ Harness dashboard loaded
☐ GitHub repo accessible
☐ Test commit prepared
☐ Previous run logs available
☐ Artifacts downloaded (JAR, reports)
☐ Network stable
☐ Screen sharing tested
☐ Cheat sheet open
```

**5 Minutes Before:**
```
☐ Close unnecessary tabs
☐ Disable notifications
☐ Check microphone
☐ Full screen browser
☐ Have water ready
☐ Deep breath - you got this! 💪
```

---

## 🎯 Focus Points

**Most Important Things to Communicate:**

1. **Automation** → Push code, automatic checks, ready to deploy
2. **Security** → Three layers catch everything
3. **Consistency** → Same checks for everyone, every time  
4. **Speed** → 87.5% faster than manual
5. **Scalability** → 52 projects, one central update

**Don't Get Lost In:**
- YAML syntax details
- Maven internals
- Tool-specific configs
- Infrastructure setup

**Focus On:**
- Business value
- Time savings
- Security benefits
- Developer experience
- Live execution

---

**YOU GOT THIS! 🚀**

Remember: You built something amazing. Be confident, be clear, be concise!
