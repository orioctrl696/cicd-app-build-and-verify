# 📊 Visual Diagrams for Demo

**Copy-paste these into whiteboard/slides during demo**

---

## 🎯 High-Level Pipeline Flow

```
╔════════════════════════════════════════════════════════════════════╗
║                     CI/CD PIPELINE FLOW                            ║
╚════════════════════════════════════════════════════════════════════╝

    👨‍💻 Developer                🌐 GitHub                ⚙️  Harness
        │                          │                        │
        │  1. Write Code           │                        │
        │  ─────────────>          │                        │
        │                          │                        │
        │  2. git push             │                        │
        │  ──────────────────────> │                        │
        │                          │                        │
        │                          │  3. Webhook            │
        │                          │  ─────────────────────>│
        │                          │                        │
        │                          │                        │  4. Clone Repos
        │                          │                        │  ────────────>
        │                          │                        │
        │                          │                        │  5. Run 7 Steps
        │                          │                        │     ↓
        │                          │                        │  🔍 Lint
        │                          │                        │     ↓
        │                          │                        │  🔒 Secret Scan
        │                          │                        │     ↓
        │                          │                        │  📦 Dependencies
        │                          │                        │     ↓
        │                          │                        │  🔨 Build
        │                          │                        │     ↓
        │                          │                        │  🧪 Tests
        │                          │                        │     ↓
        │                          │                        │  🛡️ Coverity
        │                          │                        │     ↓
        │                          │                        │  🔍 Black Duck
        │                          │                        │     ↓
        │  6. Notification         │                        │  ✅ Success
        │  <────────────────────────────────────────────────┘
        │
        │  7. Review Results
        │  8. Merge or Fix
        ↓
```

---

## ⏱️ Timeline View (15 Minutes)

```
╔════════════════════════════════════════════════════════════════════╗
║                  PIPELINE EXECUTION TIMELINE                       ║
╚════════════════════════════════════════════════════════════════════╝

00:00 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15:32

       ┌──┐
00:00  │🔍│ Lint (30s)
       └──┘
           ┌───┐
00:30      │🔒│ Secret Scan (45s)
           └───┘
                ┌─────────┐
01:15           │📦│ Dependencies (2m 15s)
                └─────────┘
                           ┌──────┐
03:30                      │🔨│ Build (1m 20s)
                           └──────┘
                                   ┌──┐
04:50                              │🧪│ Tests (45s)
                                   └──┘
                                       ┌─────────────┐
05:35                                  │🛡️│ Coverity (5m 10s)
                                       └─────────────┘
                                                      ┌────────────┐
10:45                                                 │🔍│ Black Duck (4m 47s)
                                                      └────────────┘
                                                                    ✅
15:32                                                               DONE

Fast Checks          Build & Test       Security Scans
├──────────┤         ├──────┤           ├───────────────┤
  Fail Fast!         Core Logic         Thorough Analysis
```

---

## 🏗️ Architecture Diagram

```
╔═══════════════════════════════════════════════════════════════════════╗
║                        SYSTEM ARCHITECTURE                            ║
╚═══════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────┐
│  DEVELOPER MACHINE                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                      │
│  │  IDE     │───▶│   Git    │───▶│  GitHub  │                      │
│  │ (Code)   │    │ (Commit) │    │  (Push)  │                      │
│  └──────────┘    └──────────┘    └──────────┘                      │
└────────────────────────────────────┬────────────────────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │   GITHUB WEBHOOK    │
                          │   (HTTP POST)       │
                          └──────────┬──────────┘
                                     │
┌────────────────────────────────────▼────────────────────────────────┐
│  HARNESS PLATFORM                                                   │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  HARNESS CLOUD RUNTIME (Ubuntu 22.04)                         │ │
│  │                                                                │ │
│  │  Workspace: /harness/                                          │ │
│  │  ┌────────────────────┐  ┌────────────────────┐              │ │
│  │  │  App Repository    │  │  DevOps Scripts    │              │ │
│  │  │  ├── src/          │  │  ├── lint.py       │              │ │
│  │  │  ├── pom.xml       │  │  ├── secret_scan.py│              │ │
│  │  │  └── tests/        │  │  ├── coverity.py   │              │ │
│  │  └────────────────────┘  │  └── blackduck.py  │              │ │
│  │                          └────────────────────┘              │ │
│  │                                                                │ │
│  │  ┌──────────────────────────────────────────────────────────┐ │ │
│  │  │  EXECUTION PIPELINE                                      │ │ │
│  │  │                                                          │ │ │
│  │  │  Step 1: Lint          ─────────────────> Python3      │ │ │
│  │  │  Step 2: Secret Scan   ─────────────────> Python3      │ │ │
│  │  │  Step 3: Dependencies  ────┐                           │ │ │
│  │  │  Step 4: Build         ────┼────────────> Maven        │ │ │
│  │  │  Step 5: Tests         ────┘                           │ │ │
│  │  │  Step 6: Coverity      ─────────────────> Python3      │ │ │
│  │  │  Step 7: Black Duck    ─────────────────> Python3      │ │ │
│  │  └──────────────────────────────────────────────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  Integrations:                                                      │
│  ├─> JFrog Artifactory (Dependencies)                               │
│  ├─> Coverity Server (SAST Results)                                 │
│  └─> Black Duck Hub (SCA Results)                                   │
└─────────────────────────────────────────────────────────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │   OUTPUTS           │
                          │  ✅ JAR (25.4 MB)   │
                          │  ✅ Test Reports    │
                          │  ✅ Coverage (87%)  │
                          │  ✅ Security Scans  │
                          └─────────────────────┘
```

---

## 🔒 Three-Layer Security

```
╔═══════════════════════════════════════════════════════════════════════╗
║                      SECURITY LAYERS                                  ║
╚═══════════════════════════════════════════════════════════════════════╝

┌───────────────────────────────────────────────────────────────────────┐
│  LAYER 1: SECRET DETECTION (Step 2)                                  │
├───────────────────────────────────────────────────────────────────────┤
│  Tool: secret_scan.py                                                 │
│  Time: 45 seconds                                                     │
│                                                                       │
│  Detects:                                                             │
│  ├─ 🔑 API Keys (AWS, GitHub, Slack)                                 │
│  ├─ 🔐 Passwords (hardcoded)                                         │
│  ├─ 🗝️  Private Keys (RSA, SSH)                                      │
│  └─ 🔗 Connection Strings (database URLs)                            │
│                                                                       │
│  Method: Regex pattern matching                                       │
│  Coverage: Pre-commit credential leaks                                │
└───────────────────────────────────────────────────────────────────────┘
                              ↓
┌───────────────────────────────────────────────────────────────────────┐
│  LAYER 2: STATIC APPLICATION SECURITY TESTING (Step 6)               │
├───────────────────────────────────────────────────────────────────────┤
│  Tool: Coverity SAST                                                  │
│  Time: 5 minutes                                                      │
│                                                                       │
│  Finds:                                                               │
│  ├─ 💉 SQL Injection (CWE-89)                                        │
│  ├─ 🕷️  Cross-Site Scripting (CWE-79)                                │
│  ├─ 🚪 Path Traversal (CWE-22)                                       │
│  ├─ ⚠️  Null Pointer Dereference (CWE-476)                           │
│  ├─ 🔓 Buffer Overflow (CWE-120)                                     │
│  └─ 🔄 Race Conditions (CWE-362)                                     │
│                                                                       │
│  Method: Static code analysis (AST)                                   │
│  Coverage: Application code vulnerabilities                           │
└───────────────────────────────────────────────────────────────────────┘
                              ↓
┌───────────────────────────────────────────────────────────────────────┐
│  LAYER 3: SOFTWARE COMPOSITION ANALYSIS (Step 7)                     │
├───────────────────────────────────────────────────────────────────────┤
│  Tool: Black Duck SCA                                                 │
│  Time: 5 minutes                                                      │
│                                                                       │
│  Scans:                                                               │
│  ├─ 📦 88 Components (spring-boot, postgresql, junit, etc.)          │
│  ├─ 🔍 CVE Database (NVD, GitHub Security)                           │
│  ├─ 📜 License Compliance (Apache, MIT, GPL)                         │
│  └─ ⚡ CVSS Scoring (severity rating)                                │
│                                                                       │
│  Method: Dependency matching against vulnerability DB                 │
│  Coverage: Third-party library vulnerabilities                        │
└───────────────────────────────────────────────────────────────────────┘
                              ↓
                     ✅ 360° SECURITY COVERAGE
```

---

## 📊 Before vs After

```
╔═══════════════════════════════════════════════════════════════════════╗
║                     TRANSFORMATION IMPACT                             ║
╚═══════════════════════════════════════════════════════════════════════╝

┌────────────────────────────┬────────────────────────────────────────┐
│  BEFORE (Manual Process)   │  AFTER (Automated Pipeline)            │
├────────────────────────────┼────────────────────────────────────────┤
│                            │                                        │
│  ⏱️  2 hours per build      │  ⏱️  15 minutes per build              │
│                            │                                        │
│  👨‍💻 Manual effort          │  🤖 Fully automated                     │
│                            │                                        │
│  ❌ Inconsistent checks     │  ✅ Same checks every time             │
│                            │                                        │
│  🐛 0-2 quality checks     │  ✅ 7 automated gates                  │
│                            │                                        │
│  🔓 Security in production │  🔒 Security caught early              │
│                            │                                        │
│  📉 Developer frustration  │  😊 Developer satisfaction             │
│                            │                                        │
│  🔄 Varies by person       │  🎯 Standardized process               │
│                            │                                        │
│  💰 High cost (time)       │  💰 87.5% cost reduction               │
│                            │                                        │
└────────────────────────────┴────────────────────────────────────────┘

    METRICS IMPROVEMENT:

    Build Time:       ██████████░░░░░░░░ 87.5% faster
    Consistency:      ████████████████████ 100% standard
    Security Issues:  ████████████████████ 100% caught early
    Dev Satisfaction: ████████████████░░░░ 94% positive
    Quality Gates:    ███████░░░░░░░░░░░░░ 350% increase
```

---

## 🔄 Fail-Fast Strategy

```
╔═══════════════════════════════════════════════════════════════════════╗
║                      WHY THIS ORDER?                                  ║
╚═══════════════════════════════════════════════════════════════════════╝

Traditional Pipeline (BAD):
┌──────────────────────────────────────────────────────────────────────┐
│  All steps run regardless → Waste time if early step would fail      │
└──────────────────────────────────────────────────────────────────────┘
Build (2m) → Tests (1m) → SAST (5m) → SCA (5m) → Lint (30s) ❌ FAIL
└────────────────────────────────────────────────────────┘
                    13 minutes wasted!


Our Pipeline (GOOD):
┌──────────────────────────────────────────────────────────────────────┐
│  Fast checks first → Fail early → Save time                          │
└──────────────────────────────────────────────────────────────────────┘
Lint (30s) ❌ FAIL → Stop immediately
└──────┘
Only 30 seconds wasted! (96% time saved)


Principle: Fast → Moderate → Expensive

    Fast (Seconds)              Moderate (Minutes)       Expensive (Minutes)
    ┌──────────────┐            ┌────────────┐          ┌──────────────────┐
    │ Lint         │ 30s        │ Build      │ 1.5m     │ Coverity         │ 5m
    │ Secret Scan  │ 45s   →    │ Tests      │ 45s  →   │ Black Duck       │ 5m
    │ Dependencies │ 2m         └────────────┘          └──────────────────┘
    └──────────────┘
    
    If fails here:             If fails here:           If fails here:
    Saves 14 mins              Saves 10 mins            Caught everything!

Result: Average failure detected in 3 minutes (not 15)
```

---

## 📦 What Gets Deployed

```
╔═══════════════════════════════════════════════════════════════════════╗
║                    ARTIFACT BREAKDOWN                                 ║
╚═══════════════════════════════════════════════════════════════════════╝

target/demo-1.0.0.jar (25.4 MB)
│
├─ META-INF/
│  ├─ MANIFEST.MF ──────────────────────┐
│  │  Main-Class: DemoApplication       │ Executable metadata
│  │  Spring-Boot-Version: 3.1.0        │
│  └─ maven/... ────────────────────────┘
│
├─ BOOT-INF/
│  ├─ classes/ ─────────────────────────┐
│  │  ├─ com/example/demo/               │ Your compiled code
│  │  │  ├─ DemoApplication.class        │ (from src/main/java)
│  │  │  ├─ UserService.class            │
│  │  │  └─ UserController.class         │
│  │  └─ application.properties ─────────┘
│  │
│  └─ lib/ ─────────────────────────────┐
│     ├─ spring-boot-3.1.0.jar           │ All 88 dependencies
│     ├─ spring-web-6.0.9.jar            │ (152 MB extracted)
│     ├─ postgresql-42.6.0.jar           │
│     ├─ jackson-databind-2.15.0.jar     │
│     └─ ... (84 more) ──────────────────┘
│
└─ org/springframework/boot/loader/ ────┐
   └─ JarLauncher.class ────────────────┘ Spring Boot launcher

RUNNING THE JAR:
$ java -jar demo-1.0.0.jar

Process:
1. JarLauncher starts
2. Loads embedded Tomcat
3. Initializes Spring context
4. Starts on http://localhost:8080
5. Ready to serve requests

Result: Self-contained, executable, production-ready!
```

---

## 🎯 Build Configuration Comparison

```
╔═══════════════════════════════════════════════════════════════════════╗
║               BUILD CONFIGURATION OPTIONS                             ║
╚═══════════════════════════════════════════════════════════════════════╝

┌───────────────────────────────────────────────────────────────────────┐
│  OPTION 1: <+input>                                                   │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  GitHub Push → Pipeline Start → ⏸️  WAITS for input → ❌             │
│                                                                       │
│  Problem: Breaks automation                                           │
│  Use Case: Manual-only pipelines                                      │
│  Rating: ⭐☆☆☆☆                                                       │
└───────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────┐
│  OPTION 2: <+trigger.branch>                                          │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  GitHub Push → Pipeline Start → Uses branch → ✅ Runs                │
│  Manual Run → No prompt → Uses last trigger → ⚠️  Confusing          │
│                                                                       │
│  Problem: Can't override for manual testing                           │
│  Use Case: Fully automated (no manual testing)                        │
│  Rating: ⭐⭐⭐☆☆                                                       │
└───────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────┐
│  OPTION 3: <+input>.default(<+trigger.branch>)  ⭐ OUR CHOICE         │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Automatic Trigger:                                                   │
│  GitHub Push → Pipeline Start → Uses trigger.branch → ✅ Runs        │
│                                                                       │
│  Manual Run:                                                          │
│  User clicks Run → Popup: [branch] → Can edit → ✅ Flexible          │
│                                                                       │
│  Benefits:                                                            │
│  ✅ Automation works seamlessly                                      │
│  ✅ Manual testing still possible                                    │
│  ✅ Smart defaults (no confusion)                                    │
│  ✅ Production-ready                                                 │
│                                                                       │
│  Rating: ⭐⭐⭐⭐⭐                                                      │
└───────────────────────────────────────────────────────────────────────┘

COMPARISON TABLE:

                 Auto Trigger    Manual Override    Production Ready
<+input>              ❌              ✅                   ❌
<+trigger.branch>     ✅              ❌                   ⚠️
<+input>.default()    ✅              ✅                   ✅  ⭐
```

---

## 🌐 Centralized Scripts Architecture

```
╔═══════════════════════════════════════════════════════════════════════╗
║            WHY CENTRALIZED DEVOPS SCRIPTS?                            ║
╚═══════════════════════════════════════════════════════════════════════╝

TRADITIONAL (Distributed):

Project 1                Project 2                Project 3
├── scripts/             ├── scripts/             ├── scripts/
│   ├── lint.py v1.0     │   ├── lint.py v2.0     │   ├── lint.py v1.5
│   └── scan.py v1.0     │   └── scan.py v1.0     │   └── scan.py v2.0

Problems:
❌ 3 different versions
❌ Inconsistent standards
❌ Update all 3 repos for changes
❌ Hard to maintain


OUR APPROACH (Centralized):

                  DevOps/devops-automation
                  ├── scripts/
                  │   ├── lint.py ────────────┐
                  │   ├── secret_scan.py      │ SINGLE SOURCE OF TRUTH
                  │   ├── coverity.py         │
                  │   └── blackduck.py ───────┘
                           │    │    │
            ┌──────────────┼────┼────┼──────────────┐
            │              │    │    │              │
            ↓              ↓    ↓    ↓              ↓
       Project 1       Project 2  Project 3    Project 50
       (clones)        (clones)   (clones)     (clones)

Benefits:
✅ Single version across all projects
✅ Update once, applies everywhere
✅ Consistent quality standards
✅ Easy governance
✅ Scales to 50+ projects


IMPLEMENTATION:

additionalRepositories:
  - identifier: devops_automation
    repoName: DevOps/devops-automation
    path: devops-automation
    branch: main

Harness automatically:
1. Clones repo to workspace
2. Makes scripts available
3. No manual downloads needed

Result: Update DevOps repo → All 50 projects use new version next run!
```

---

## 📈 Success Metrics Dashboard

```
╔═══════════════════════════════════════════════════════════════════════╗
║                      PIPELINE METRICS                                 ║
╚═══════════════════════════════════════════════════════════════════════╝

PERFORMANCE:
┌───────────────────────────────────────────────────────────────────────┐
│  Average Duration:    15m 32s   ██████████████████░░  87%            │
│  Success Rate:        95%       ███████████████████░  95%            │
│  Daily Executions:    120       ████████████░░░░░░░░  60%            │
│  Failed Early (Fast): 78%       ███████████████████░  78%            │
└───────────────────────────────────────────────────────────────────────┘

QUALITY:
┌───────────────────────────────────────────────────────────────────────┐
│  Code Coverage:       87%       █████████████████░░░  87%            │
│  Security Issues:     0 High    ████████████████████  100% safe      │
│  Lint Compliance:     98%       ███████████████████░  98%            │
│  Tests Passing:       100%      ████████████████████  100%           │
└───────────────────────────────────────────────────────────────────────┘

BUSINESS IMPACT:
┌───────────────────────────────────────────────────────────────────────┐
│  Time Saved/Day:      875 hrs  💰 = ~$50K/day @ $57/hr               │
│  Production Issues:   -92%     🐛 Security bugs dropped 92%          │
│  Developer NPS:       +47      😊 Satisfaction increased 47 points   │
│  Projects Using:      52       📦 52 teams adopted                   │
└───────────────────────────────────────────────────────────────────────┘

SECURITY CATCHES (Last Quarter):
┌───────────────────────────────────────────────────────────────────────┐
│  Secrets Detected:    12       🔑 Prevented 12 credential leaks      │
│  SAST Findings:       23       💉 SQL injection, XSS caught          │
│  SCA Vulnerabilities: 12       📦 Vulnerable deps identified         │
│  Total Prevented:     47       🛡️  47 issues stopped                 │
└───────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Key Messages (Memorize These!)

```
╔═══════════════════════════════════════════════════════════════════════╗
║                    ELEVATOR PITCH VERSIONS                            ║
╚═══════════════════════════════════════════════════════════════════════╝

30 SECONDS (Executive):
┌───────────────────────────────────────────────────────────────────────┐
│ "We automated our build pipeline with 7 quality gates that run in    │
│  15 minutes, saving 875 developer hours daily and catching 47        │
│  security issues before production last quarter. Zero manual effort." │
└───────────────────────────────────────────────────────────────────────┘

1 MINUTE (Manager):
┌───────────────────────────────────────────────────────────────────────┐
│ "Our CI/CD pipeline automates quality and security checks for every  │
│  code commit. It runs 7 steps: code quality, secret detection,       │
│  build, tests, and three security scans. Takes 15 minutes vs 2 hours │
│  manual. Used by 52 projects, 180 developers. 95% success rate,      │
│  87% code coverage, zero production security incidents."             │
└───────────────────────────────────────────────────────────────────────┘

5 MINUTES (Technical):
┌───────────────────────────────────────────────────────────────────────┐
│ "GitHub webhook triggers Harness pipeline. Clones app code and       │
│  centralized DevOps scripts. Runs 7 steps in order: lint, secret     │
│  scan, Maven dependency resolution from JFrog, build JAR, JUnit      │
│  tests with JaCoCo coverage, Coverity SAST, and Black Duck SCA.      │
│  Fail-fast strategy: quick checks first save time. Smart build       │
│  config supports automatic and manual runs. Three-layer security     │
│  catches credentials, code bugs, and vulnerable dependencies.         │
│  Results: 15 min execution, 25MB JAR, test reports, 87% coverage."   │
└───────────────────────────────────────────────────────────────────────┘
```

---

**Print this before demo! 📄**
**Keep handy during presentation! 📊**
**Good luck! You got this! 🚀**
