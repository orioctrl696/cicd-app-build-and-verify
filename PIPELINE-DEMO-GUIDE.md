# 🚀 CI/CD Pipeline Demo - Complete Guide

**Pipeline Name:** SpringBoot Build and Verify  
**Purpose:** Automated quality gates for Spring Boot applications  
**Demo Date:** 2026-11-19

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [End-to-End Flow](#end-to-end-flow)
4. [Step-by-Step Logic](#step-by-step-logic)
5. [Key Features](#key-features)
6. [Demo Script](#demo-script)
7. [Q&A Preparation](#qa-preparation)

---

## 🎯 Overview

### **What Problem Does This Solve?**

**Before Pipeline:**
```
❌ Manual code quality checks
❌ Inconsistent security scanning
❌ Time-consuming manual builds
❌ Tests run only on developer machines
❌ Security vulnerabilities slip to production
❌ No standardized process
```

**After Pipeline:**
```
✅ Automated quality gates (7 steps)
✅ Consistent security scanning (3 layers)
✅ Fast, reliable builds (15 minutes)
✅ Tests run on every commit
✅ Security issues caught early
✅ Standardized, repeatable process
```

### **Business Value:**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Build Time** | 2 hours (manual) | 15 minutes | 88% faster |
| **Security Issues** | Found in production | Caught in pipeline | 100% early detection |
| **Manual Effort** | Every commit | Zero | 100% automated |
| **Consistency** | Varies by developer | Same every time | 100% standardized |
| **Quality Gates** | 0-2 | 7 automated | 350% improvement |

---

## 🏗️ Architecture

### **High-Level Architecture:**

```
┌─────────────────────────────────────────────────────────────────┐
│                         DEVELOPER                               │
│                    (Writes Code & Pushes)                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GITHUB ENTERPRISE                           │
│                  (github.aepsc.com)                             │
│                                                                 │
│  Repositories:                                                  │
│  1. cicd-app-build-and-verify     (Application Code)          │
│  2. DevOps/devops-automation      (Shared Scripts)            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                        WEBHOOK TRIGGER
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      HARNESS PLATFORM                           │
│                    (Pipeline Orchestration)                     │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              HARNESS CLOUD RUNTIME                       │  │
│  │                                                          │  │
│  │  Workspace:                                              │  │
│  │  ├── /harness/                                           │  │
│  │  │   ├── src/          (App code - Repo 1)              │  │
│  │  │   ├── pom.xml                                         │  │
│  │  │   └── devops-automation/  (Scripts - Repo 2)         │  │
│  │  │       └── scripts/                                    │  │
│  │  │           ├── lint.py                                 │  │
│  │  │           ├── secret_scan.py                          │  │
│  │  │           ├── coverity.py                             │  │
│  │  │           └── blackduck.py                            │  │
│  │                                                          │  │
│  │  Execution Pipeline:                                     │  │
│  │  ┌────────────────────────────────────────────────┐     │  │
│  │  │  Step 1: Lint (Code Quality)                   │     │  │
│  │  ├────────────────────────────────────────────────┤     │  │
│  │  │  Step 2: Secret Scan (Security)                │     │  │
│  │  ├────────────────────────────────────────────────┤     │  │
│  │  │  Step 3: Dependencies (Maven + JFrog)          │     │  │
│  │  ├────────────────────────────────────────────────┤     │  │
│  │  │  Step 4: Build (Create JAR)                    │     │  │
│  │  ├────────────────────────────────────────────────┤     │  │
│  │  │  Step 5: Unit Tests (JUnit)                    │     │  │
│  │  ├────────────────────────────────────────────────┤     │  │
│  │  │  Step 6: Coverity SAST (Security)              │     │  │
│  │  ├────────────────────────────────────────────────┤     │  │
│  │  │  Step 7: Black Duck SCA (Dependencies)         │     │  │
│  │  └────────────────────────────────────────────────┘     │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         OUTPUTS                                 │
│                                                                 │
│  ✅ Deployable JAR artifact (target/*.jar)                     │
│  ✅ Test reports (target/surefire-reports/)                    │
│  ✅ Coverage reports (target/site/jacoco/)                     │
│  ✅ Security scan results (Coverity, Black Duck)               │
│  ✅ Pipeline execution logs                                     │
└─────────────────────────────────────────────────────────────────┘
```

### **Component Breakdown:**

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Source Control** | GitHub Enterprise | Version control, webhook triggers |
| **CI/CD Platform** | Harness | Pipeline orchestration, execution |
| **Runtime** | Harness Cloud | Isolated build environment |
| **Build Tool** | Maven 3.8+ | Dependency management, build, test |
| **Language** | Java 17 | Application runtime |
| **Artifact Repository** | JFrog Artifactory | Dependency resolution |
| **Code Quality** | Custom lint.py | Style, standards enforcement |
| **Secret Detection** | Custom secret_scan.py | Credential leak prevention |
| **SAST** | Coverity | Static security analysis |
| **SCA** | Black Duck | Dependency vulnerability scanning |
| **Testing** | JUnit 5 + JaCoCo | Unit tests, coverage |

---

## 🔄 End-to-End Flow

### **Complete Journey: Code to Deployment**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: DEVELOPER WORKFLOW                                             │
└─────────────────────────────────────────────────────────────────────────┘

Developer Machine
    │
    ├── 1. Developer writes code
    │      File: UserService.java
    │
    ├── 2. Local testing (optional)
    │      $ mvn clean test
    │
    ├── 3. Commits code
    │      $ git add .
    │      $ git commit -m "Add user service"
    │
    └── 4. Pushes to GitHub
           $ git push origin feature/user-service


┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: TRIGGER ACTIVATION                                             │
└─────────────────────────────────────────────────────────────────────────┘

GitHub Enterprise (github.aepsc.com)
    │
    ├── 5. Receives push event
    │      Branch: feature/user-service
    │      Commit: a1b2c3d
    │
    ├── 6. Webhook configured
    │      URL: https://app.harness.io/gateway/...
    │
    └── 7. Sends HTTP POST
           Payload: {
             "event": "push",
             "branch": "feature/user-service",
             "commit": "a1b2c3d",
             "author": "developer@company.com"
           }


┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: PIPELINE INITIALIZATION                                        │
└─────────────────────────────────────────────────────────────────────────┘

Harness Platform
    │
    ├── 8. Receives webhook
    │      Trigger: github_auto_trigger
    │
    ├── 9. Validates trigger
    │      Type: Any (matches all events)
    │      Connector: github_app_connector ✅
    │
    ├── 10. Reads pipeline YAML
    │       File: app-build-verify.yaml
    │
    ├── 11. Sets variables
    │       triggerType: "push"
    │       build branch: "feature/user-service"
    │
    └── 12. Allocates cloud resources
            Runtime: Harness Cloud
            Container: Ubuntu 22.04
            CPU: 2 cores
            Memory: 4 GB


┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: REPOSITORY CLONING                                             │
└─────────────────────────────────────────────────────────────────────────┘

Harness Cloud Workspace
    │
    ├── 13. Clones PRIMARY repository
    │       Repo: cicd-app-build-and-verify
    │       Branch: feature/user-service
    │       Path: /harness/
    │       ✅ src/, pom.xml, README.md cloned
    │
    └── 14. Clones ADDITIONAL repository
            Repo: DevOps/devops-automation
            Branch: main
            Path: /harness/devops-automation/
            ✅ scripts/ folder cloned


┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 5: EXECUTION - 7 QUALITY GATES                                    │
└─────────────────────────────────────────────────────────────────────────┘

STEP 1/7: 🔍 LINT (Code Quality)
────────────────────────────────
Time: 00:00 - 00:30 (30 seconds)

Command: python3 devops-automation/scripts/lint.py

Process:
  ├── Scans all .java files
  ├── Checks code style (indentation, naming)
  ├── Finds TODO comments
  ├── Validates line length (<120 chars)
  └── Generates report

Output:
  ✅ 145 files scanned
  ✅ 2 warnings (TODO comments)
  ✅ 0 errors
  Status: PASSED ✅

Why: Ensures consistent code quality before proceeding


STEP 2/7: 🔒 SECRET SCAN (Security Layer 1)
────────────────────────────────────────────
Time: 00:30 - 01:15 (45 seconds)

Command: python3 devops-automation/scripts/secret_scan.py

Process:
  ├── Scans all files for patterns
  ├── Regex patterns:
  │   ├── API keys (ghp_, sk-test-)
  │   ├── AWS credentials (AKIA...)
  │   ├── Passwords (password=...)
  │   └── Database URLs (jdbc:...)
  └── Checks git history

Output:
  ✅ 156 files scanned
  ✅ 0 secrets found
  Status: PASSED ✅

Why: Prevents credential leaks before code review


STEP 3/7: 📦 DEPENDENCIES (Maven Resolution)
─────────────────────────────────────────────
Time: 01:15 - 03:30 (2 minutes 15 seconds)

Command: mvn dependency:resolve -B

Process:
  ├── Reads pom.xml
  ├── Connects to JFrog Artifactory
  │   URL: https://artifactory.company.com
  │   Auth: <+secrets.jfrog_username/password>
  ├── Downloads dependencies:
  │   ├── spring-boot-starter-web (15 MB)
  │   ├── spring-boot-starter-data-jpa (8 MB)
  │   ├── postgresql (2 MB)
  │   ├── junit-jupiter (5 MB)
  │   └── ... (88 components total)
  └── Caches in ~/.m2/repository/

Output:
  ✅ Downloaded 88 components (152 MB)
  ✅ All dependencies resolved
  Status: PASSED ✅

Why: Ensures all libraries available before build


STEP 4/7: 🔨 BUILD (Application Compilation)
────────────────────────────────────────────
Time: 03:30 - 04:50 (1 minute 20 seconds)

Command: mvn clean package -DskipTests -B

Process:
  ├── mvn clean
  │   └── Deletes target/ directory
  ├── mvn compile
  │   ├── Compiles src/main/java/ → target/classes/
  │   └── 47 Java files compiled
  ├── mvn package
  │   ├── Creates JAR file
  │   ├── Includes compiled classes
  │   ├── Includes resources
  │   └── Manifest file generation
  └── -DskipTests (tests run separately)

Output:
  ✅ Compilation successful
  ✅ JAR created: target/demo-1.0.0.jar (25.4 MB)
  ✅ Executable JAR with dependencies
  Status: PASSED ✅

Why: Creates deployable artifact, validates code compiles


STEP 5/7: 🧪 UNIT TESTS (Quality Validation)
────────────────────────────────────────────
Time: 04:50 - 05:35 (45 seconds)

Command: mvn test -B

Process:
  ├── Compiles test code
  │   └── src/test/java/ → target/test-classes/
  ├── Discovers test files
  │   ├── *Test.java pattern
  │   └── Found: 12 test classes
  ├── Executes tests
  │   ├── DemoApplicationTests (1 test)
  │   ├── UserServiceTest (4 tests)
  │   ├── UserControllerTest (3 tests)
  │   └── ... (8 more classes)
  ├── JaCoCo measures coverage
  │   ├── Instruments bytecode
  │   ├── Tracks execution
  │   └── Generates report
  └── Results aggregation

Output:
  ✅ Tests run: 23
  ✅ Failures: 0
  ✅ Errors: 0
  ✅ Skipped: 0
  ✅ Coverage: 87%
  ✅ Report: target/site/jacoco/index.html
  Status: PASSED ✅

Why: Validates business logic, prevents regressions


STEP 6/7: 🛡️ COVERITY SAST (Security Layer 2)
──────────────────────────────────────────────
Time: 05:35 - 10:45 (5 minutes 10 seconds)

Command: python3 devops-automation/scripts/coverity.py

Process:
  ├── Coverity Build
  │   ├── Instruments source code
  │   └── Creates intermediate model
  ├── Coverity Analyze
  │   ├── Checks for vulnerabilities:
  │   │   ├── SQL injection
  │   │   ├── Cross-site scripting (XSS)
  │   │   ├── Null pointer dereference
  │   │   ├── Buffer overflow
  │   │   ├── Resource leaks
  │   │   ├── Concurrency issues
  │   │   └── Path traversal
  │   └── Severity scoring (High/Medium/Low)
  └── Upload results to Coverity server

Output:
  ✅ 47 files analyzed
  ✅ 0 High severity issues
  ✅ 2 Medium severity (informational)
  ✅ 5 Low severity (code quality)
  Status: PASSED ✅

Why: Static code analysis catches security bugs early


STEP 7/7: 🔍 BLACK DUCK SCA (Security Layer 3)
───────────────────────────────────────────────
Time: 10:45 - 15:32 (4 minutes 47 seconds)

Command: python3 devops-automation/scripts/blackduck.py

Process:
  ├── Dependency Scan
  │   ├── Reads pom.xml dependencies
  │   ├── 88 components identified
  │   └── Transitive dependencies included
  ├── Black Duck Analysis
  │   ├── Checks CVE database
  │   ├── Known vulnerability matching
  │   ├── License compliance check
  │   └── Component security rating
  ├── Risk Assessment
  │   ├── CVSS scoring
  │   └── Severity classification
  └── Upload to Black Duck Hub

Output:
  ✅ 88 components scanned
  ✅ 0 High risk vulnerabilities
  ✅ 1 Medium risk (known, patched)
  ✅ 2 Low risk (acceptable)
  ✅ All licenses compliant (Apache 2.0, MIT)
  Status: PASSED ✅

Why: Prevents vulnerable dependencies in production


┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 6: RESULTS & ARTIFACTS                                            │
└─────────────────────────────────────────────────────────────────────────┘

Pipeline Completion
    │
    ├── 15. All steps passed ✅
    │       Total time: 15 minutes 32 seconds
    │
    ├── 16. Artifacts generated
    │       ├── demo-1.0.0.jar (deployable)
    │       ├── Test reports (HTML)
    │       ├── Coverage report (87%)
    │       ├── Security scan results
    │       └── Build logs
    │
    ├── 17. Notifications sent
    │       ├── Email: developer@company.com
    │       ├── Slack: #dev-team channel
    │       └── Status: ✅ SUCCESS
    │
    └── 18. Ready for next stage
            Options:
            ├── Deploy to DEV environment
            ├── Manual approval for QA
            └── Trigger integration tests


┌─────────────────────────────────────────────────────────────────────────┐
│ PHASE 7: NEXT ACTIONS                                                   │
└─────────────────────────────────────────────────────────────────────────┘

Developer sees results
    │
    ├── GitHub PR updated
    │   └── ✅ All checks passed
    │
    ├── Harness dashboard
    │   └── Green checkmarks on all steps
    │
    └── Decision made
        ├── If SUCCESS → Merge PR to main
        ├── If FAILURE → Review logs, fix issues
        └── If WARNINGS → Review, decide to proceed
```

---

## 🔧 Step-by-Step Logic

### **Why This Order?**

The 7 steps follow a **fail-fast** strategy:

```
Fast Checks First (30s - 2min)
    ├── Step 1: Lint (30s) → Fast, fails early
    ├── Step 2: Secret Scan (45s) → Critical security
    └── Step 3: Dependencies (2m) → Required for build

Build & Test (3-5 min)
    ├── Step 4: Build (1.5m) → Creates artifact
    └── Step 5: Tests (45s) → Validates functionality

Expensive Scans Last (10 min)
    ├── Step 6: Coverity (5m) → Deep security analysis
    └── Step 7: Black Duck (5m) → Dependency check

Total: ~15 minutes
```

**Logic:** If lint fails in 30 seconds, why waste 15 minutes on full pipeline?

---

### **Step 1: Lint - Deep Dive**

**What it checks:**
```python
# lint.py logic (simplified)

def check_code_quality(files):
    issues = []
    
    for file in files:
        # Check 1: Line length
        for line in file:
            if len(line) > 120:
                issues.append(f"{file}:{line_no} - Line too long")
        
        # Check 2: Naming conventions
        if not follows_naming_convention(file):
            issues.append(f"{file} - Bad naming")
        
        # Check 3: TODO comments
        if "TODO" in file or "FIXME" in file:
            issues.append(f"{file} - Has TODO/FIXME")
        
        # Check 4: Unused imports
        unused = find_unused_imports(file)
        issues.extend(unused)
    
    return issues
```

**Example output:**
```
Linting 145 files...
────────────────────────────────
❌ src/main/java/UserService.java:47
   Line exceeds 120 characters (current: 135)

⚠️  src/main/java/OrderController.java:23
   TODO comment found: "TODO: Add pagination"

✅ No critical issues found
✅ 2 warnings (can proceed)
```

---

### **Step 2: Secret Scan - Deep Dive**

**What it detects:**
```python
# secret_scan.py patterns

PATTERNS = {
    'aws_key': r'AKIA[0-9A-Z]{16}',
    'github_token': r'ghp_[a-zA-Z0-9]{36}',
    'slack_webhook': r'https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}',
    'password': r'password\s*=\s*["\'][^"\']+["\']',
    'api_key': r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
    'jdbc': r'jdbc:postgresql://[^:]+:\d+/[^?]+\?user=[^&]+&password=.+',
    'private_key': r'-----BEGIN (RSA |)PRIVATE KEY-----'
}

def scan_for_secrets(files):
    findings = []
    
    for file in files:
        content = read_file(file)
        
        for pattern_name, pattern in PATTERNS.items():
            matches = re.findall(pattern, content)
            
            if matches:
                findings.append({
                    'file': file,
                    'type': pattern_name,
                    'severity': 'CRITICAL',
                    'line': get_line_number(content, match)
                })
    
    return findings
```

**Example detection:**
```
Scanning 156 files for secrets...
────────────────────────────────────────────────────────
❌ CRITICAL: Secret detected!
   File: src/main/resources/application.properties
   Line: 12
   Type: password
   Value: spring.datasource.password="admin123"
   
   Action: Remove hardcoded password, use environment variables
   
🛑 Pipeline STOPPED - Security violation
```

---

### **Step 3: Dependencies - Deep Dive**

**Maven resolution process:**

```xml
<!-- pom.xml snippet -->
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <version>3.1.0</version>
    </dependency>
</dependencies>
```

**What happens:**
```
mvn dependency:resolve -B
    │
    ├── 1. Read pom.xml
    │      Dependency: spring-boot-starter-web:3.1.0
    │
    ├── 2. Check local cache
    │      Location: ~/.m2/repository/
    │      Found: NO
    │
    ├── 3. Connect to JFrog
    │      URL: https://artifactory.company.com/maven-repo
    │      Auth: Basic <base64(username:password)>
    │
    ├── 4. Download artifact
    │      spring-boot-starter-web-3.1.0.jar (15 MB)
    │      ├── Download .jar
    │      ├── Download .pom (metadata)
    │      └── Verify checksums (SHA1, MD5)
    │
    ├── 5. Resolve transitive dependencies
    │      spring-boot-starter-web depends on:
    │      ├── spring-web
    │      ├── spring-webmvc
    │      ├── jackson-databind
    │      ├── tomcat-embed-core
    │      └── ... (20 more)
    │
    └── 6. Repeat for all 88 components
           Total downloaded: 152 MB
```

**Output tree:**
```
[INFO] com.example:demo:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:3.1.0
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:3.1.0
[INFO] |  |  +- org.springframework.boot:spring-boot:jar:3.1.0
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.30
[INFO] |  +- org.springframework:spring-web:jar:6.0.9
[INFO] |  \- org.springframework:spring-webmvc:jar:6.0.9
[INFO] +- org.postgresql:postgresql:jar:42.6.0
[INFO] \- org.springframework.boot:spring-boot-starter-test:jar:3.1.0
```

---

### **Step 4: Build - Deep Dive**

**Maven build lifecycle:**

```
mvn clean package -DskipTests -B
    │
    ├── PHASE 1: clean
    │   └── Delete target/ directory
    │       ✅ Removed 1,245 files
    │
    ├── PHASE 2: validate
    │   └── Validate project structure
    │       ✅ pom.xml valid
    │
    ├── PHASE 3: compile
    │   ├── Process resources
    │   │   Copy: src/main/resources → target/classes/
    │   │   ├── application.properties
    │   │   ├── application.yml
    │   │   └── static/ folder
    │   │
    │   └── Compile Java
    │       javac -d target/classes src/main/java/**/*.java
    │       ├── UserService.java → UserService.class
    │       ├── UserController.java → UserController.class
    │       └── ... (47 files)
    │       ✅ Compiled 47 classes
    │
    ├── PHASE 4: test (SKIPPED)
    │   └── -DskipTests flag
    │
    └── PHASE 5: package
        ├── Create JAR structure
        │   target/demo-1.0.0.jar
        │   ├── META-INF/
        │   │   ├── MANIFEST.MF
        │   │   └── maven/
        │   ├── com/example/demo/
        │   │   ├── UserService.class
        │   │   └── UserController.class
        │   ├── org/springframework/... (dependencies)
        │   └── application.properties
        │
        └── Make executable
            MANIFEST.MF:
            Main-Class: com.example.demo.DemoApplication
            Start-Class: com.example.demo.DemoApplication
            Spring-Boot-Version: 3.1.0
            Spring-Boot-Classes: BOOT-INF/classes/
            Spring-Boot-Lib: BOOT-INF/lib/

✅ BUILD SUCCESS
✅ JAR: target/demo-1.0.0.jar (25.4 MB)
```

**Why skip tests here?**
- Tests run in separate step (Step 5)
- Better visibility (separate logs)
- Fail-fast: build issues vs. test issues

---

### **Step 5: Unit Tests - Deep Dive**

**Test execution flow:**

```
mvn test -B
    │
    ├── 1. Compile test code
    │      src/test/java → target/test-classes/
    │      12 test classes compiled
    │
    ├── 2. Maven Surefire Plugin
    │      Discovers tests:
    │      ├── *Test.java
    │      ├── *Tests.java
    │      └── *TestCase.java
    │
    ├── 3. JUnit 5 Execution
    │      For each test class:
    │      │
    │      ├── @BeforeAll
    │      │   └── Setup (once per class)
    │      │
    │      ├── For each @Test method:
    │      │   ├── @BeforeEach
    │      │   │   └── Setup (before each test)
    │      │   ├── Execute test
    │      │   │   ├── Arrange (setup data)
    │      │   │   ├── Act (call method)
    │      │   │   └── Assert (verify result)
    │      │   └── @AfterEach
    │      │       └── Cleanup
    │      │
    │      └── @AfterAll
    │          └── Cleanup (once per class)
    │
    ├── 4. JaCoCo Coverage
    │      Instruments bytecode:
    │      ├── Tracks which lines executed
    │      ├── Counts branch coverage
    │      └── Calculates percentages
    │
    └── 5. Generate Reports
           ├── target/surefire-reports/
           │   ├── TEST-*.xml (JUnit format)
           │   └── *.txt (readable format)
           └── target/site/jacoco/
               ├── index.html (coverage)
               ├── jacoco.xml (machine readable)
               └── jacoco.csv (data export)
```

**Example test:**
```java
@SpringBootTest
class UserServiceTest {
    
    @Autowired
    private UserService userService;
    
    @Test
    void testGetUserById() {
        // JaCoCo starts tracking here ──┐
        //                                │
        Long userId = 1L;                // Line covered ✅
        //                                │
        User user = userService          // Line covered ✅
            .getUserById(userId);        // Method called (tracked)
        //                                │
        assertNotNull(user);             // Assertion (tracked)
        assertEquals("John",             // Line covered ✅
                     user.getName());    // Line covered ✅
        //                                │
        // JaCoCo stops tracking here  ──┘
    }
}
```

**Coverage report:**
```
Package: com.example.demo.service
Class: UserService

Method Coverage:
  getUserById()     ██████████ 100% (5/5 lines)
  createUser()      ████████░░  80% (4/5 lines) - Line 47 not covered
  updateUser()      ██████████ 100% (7/7 lines)
  deleteUser()      ██████░░░░  60% (3/5 lines) - Lines 89-90 not covered

Overall: 87%
```

---

### **Step 6: Coverity SAST - Deep Dive**

**Static Analysis Process:**

```
python3 coverity.py
    │
    ├── 1. Build with instrumentation
    │      cov-build --dir idir mvn clean compile
    │      Creates: intermediate directory (idir/)
    │      ├── Captures build commands
    │      ├── Records compilation
    │      └── Generates abstract syntax tree (AST)
    │
    ├── 2. Analyze code
    │      cov-analyze --dir idir --all
    │      │
    │      ├── Security checkers:
    │      │   ├── SQL_INJECTION
    │      │   ├── XSS
    │      │   ├── PATH_TRAVERSAL
    │      │   ├── NULL_DEREFERENCE
    │      │   ├── RESOURCE_LEAK
    │      │   ├── BUFFER_OVERFLOW
    │      │   └── TOCTOU (race conditions)
    │      │
    │      ├── Quality checkers:
    │      │   ├── UNUSED_VALUE
    │      │   ├── DEADCODE
    │      │   ├── COPY_PASTE_ERROR
    │      │   └── MISSING_RETURN
    │      │
    │      └── Concurrency checkers:
    │          ├── LOCK
    │          ├── ATOMICITY
    │          └── ORDER_REVERSAL
    │
    ├── 3. Generate findings
    │      Each issue includes:
    │      ├── Type (e.g., SQL_INJECTION)
    │      ├── Severity (High/Medium/Low)
    │      ├── CWE ID (e.g., CWE-89)
    │      ├── File & line number
    │      ├── Explanation
    │      └── Fix recommendation
    │
    └── 4. Upload to Coverity Connect
           URL: https://coverity.company.com
           Project: cicd-app-build-verify
```

**Example finding:**
```
╔══════════════════════════════════════════════════════════════════╗
║ COVERITY FINDING #1                                              ║
╠══════════════════════════════════════════════════════════════════╣
║ Type: SQL_INJECTION                                              ║
║ Severity: HIGH                                                   ║
║ CWE: CWE-89 (SQL Injection)                                      ║
║ Impact: Code execution, data breach                              ║
╠══════════════════════════════════════════════════════════════════╣
║ Location:                                                        ║
║   File: src/main/java/UserRepository.java                       ║
║   Line: 45                                                       ║
║   Method: findByUsername(String username)                        ║
╠══════════════════════════════════════════════════════════════════╣
║ Issue:                                                           ║
║   String query = "SELECT * FROM users WHERE username = '"        ║
║                  + username + "'";                               ║
║   ▲ Untrusted data directly concatenated into SQL               ║
╠══════════════════════════════════════════════════════════════════╣
║ Attack Example:                                                  ║
║   username = "admin' OR '1'='1"                                  ║
║   Result: SELECT * FROM users WHERE username = 'admin'           ║
║           OR '1'='1'  ← Returns all users!                       ║
╠══════════════════════════════════════════════════════════════════╣
║ Fix:                                                             ║
║   Use PreparedStatement:                                         ║
║   String query = "SELECT * FROM users WHERE username = ?";       ║
║   PreparedStatement ps = conn.prepareStatement(query);           ║
║   ps.setString(1, username); // Safely parameterized            ║
╚══════════════════════════════════════════════════════════════════╝
```

---

### **Step 7: Black Duck SCA - Deep Dive**

**Software Composition Analysis:**

```
python3 blackduck.py
    │
    ├── 1. Detect dependencies
    │      Scans: pom.xml, package-lock.json, requirements.txt
    │      Finds: 88 components
    │
    ├── 2. Build dependency graph
    │      spring-boot-starter-web:3.1.0
    │      ├── spring-web:6.0.9
    │      │   ├── spring-core:6.0.9
    │      │   └── spring-beans:6.0.9
    │      ├── jackson-databind:2.15.0
    │      │   ├── jackson-core:2.15.0
    │      │   └── jackson-annotations:2.15.0
    │      └── ... (transitive dependencies)
    │
    ├── 3. Query Black Duck KnowledgeBase
    │      For each component:
    │      │
    │      ├── CVE Database
    │      │   Check: NVD, GitHub Security Advisories
    │      │   ├── CVE-2023-xxxxx (CRITICAL, CVSS 9.8)
    │      │   └── CVE-2022-xxxxx (HIGH, CVSS 7.5)
    │      │
    │      ├── License Check
    │      │   ├── Apache 2.0 ✅ (commercial use allowed)
    │      │   ├── MIT ✅ (permissive)
    │      │   └── GPL-3.0 ⚠️ (copyleft, legal review)
    │      │
    │      └── Component Risk
    │          ├── Operational risk (active maintenance?)
    │          ├── Version recency
    │          └── Community health
    │
    ├── 4. Risk Assessment
    │      CVSS Score Calculation:
    │      Base Score × Temporal Score × Environmental Score
    │      │
    │      ├── Attack Vector (Network/Adjacent/Local)
    │      ├── Attack Complexity (Low/High)
    │      ├── Privileges Required (None/Low/High)
    │      ├── User Interaction (None/Required)
    │      ├── Scope (Unchanged/Changed)
    │      ├── Confidentiality Impact (None/Low/High)
    │      ├── Integrity Impact (None/Low/High)
    │      └── Availability Impact (None/Low/High)
    │
    └── 5. Generate Report
           Upload to: Black Duck Hub
           URL: https://blackduck.company.com
```

**Example vulnerability:**
```
╔══════════════════════════════════════════════════════════════════╗
║ BLACK DUCK VULNERABILITY #1                                      ║
╠══════════════════════════════════════════════════════════════════╣
║ Component: jackson-databind                                      ║
║ Version: 2.12.3 (VULNERABLE)                                     ║
║ Latest Safe: 2.15.2                                              ║
╠══════════════════════════════════════════════════════════════════╣
║ CVE: CVE-2022-42003                                              ║
║ CVSS Score: 7.5 (HIGH)                                           ║
║ Published: 2022-10-02                                            ║
║ Severity: HIGH                                                   ║
╠══════════════════════════════════════════════════════════════════╣
║ Vulnerability:                                                   ║
║   Deserialization of Untrusted Data                              ║
║   Allows remote code execution via crafted JSON payload          ║
╠══════════════════════════════════════════════════════════════════╣
║ Attack Scenario:                                                 ║
║   1. Attacker sends malicious JSON                               ║
║   2. Jackson deserializes without validation                     ║
║   3. Arbitrary code executes on server                           ║
║   4. Server compromised                                          ║
╠══════════════════════════════════════════════════════════════════╣
║ Remediation:                                                     ║
║   Upgrade: jackson-databind to 2.15.2+                           ║
║   Update pom.xml:                                                ║
║   <dependency>                                                   ║
║     <groupId>com.fasterxml.jackson.core</groupId>                ║
║     <artifactId>jackson-databind</artifactId>                    ║
║     <version>2.15.2</version>                                    ║
║   </dependency>                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║ References:                                                      ║
║   - https://nvd.nist.gov/vuln/detail/CVE-2022-42003             ║
║   - https://github.com/FasterXML/jackson-databind/issues/3590   ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🎯 Key Features

### **1. Smart Build Configuration**

```yaml
build: <+input>.default(<+trigger.branch>)
```

**Intelligence:**
```
Automatic Trigger:
  Webhook → Uses <+trigger.branch> → No prompt → Fully automated ✅

Manual Trigger:
  User runs → Shows input field → Defaults to <+trigger.branch> → Can override ✅

Result: 90% automated, 10% flexible
```

**Why better than alternatives:**

| Configuration | Auto Trigger | Manual Override | Best For |
|--------------|--------------|-----------------|----------|
| `<+input>` | ❌ Always waits | ✅ Yes | Manual pipelines only |
| `<+trigger.branch>` | ✅ Yes | ❌ No | Fully automated only |
| `<+input>.default()` | ✅ Yes | ✅ Yes | **Production CI/CD** ✅ |

---

### **2. Centralized DevOps Scripts**

**Traditional Approach (BAD):**
```
Each project has its own scripts:
├── project-1/
│   └── scripts/
│       ├── lint.py (version 1)
│       └── secret_scan.py (version 1)
├── project-2/
│   └── scripts/
│       ├── lint.py (version 2 - DIFFERENT!)
│       └── secret_scan.py (version 1)
└── project-3/
    └── scripts/
        ├── lint.py (version 1 - OUTDATED!)
        └── secret_scan.py (version 3 - DIFFERENT!)

Problems:
❌ 3 different versions of lint.py
❌ Inconsistent quality checks
❌ Hard to update (3 repos to change)
❌ No central governance
```

**Our Approach (GOOD):**
```
Single source of truth:
DevOps/devops-automation/
└── scripts/
    ├── lint.py (ONE VERSION)
    ├── secret_scan.py (ONE VERSION)
    ├── coverity.py (ONE VERSION)
    └── blackduck.py (ONE VERSION)

All pipelines use additionalRepositories:
├── project-1/ → clones DevOps/devops-automation
├── project-2/ → clones DevOps/devops-automation
└── project-3/ → clones DevOps/devops-automation

Benefits:
✅ Single version across all projects
✅ Update once, applies everywhere
✅ Consistent standards
✅ Central governance
✅ Easy maintenance
```

**How it works in pipeline:**
```yaml
additionalRepositories:
  - identifier: devops_automation
    connectorRef: account.github_devops_connector
    repoName: DevOps/devops-automation
    path: devops-automation
    branch: main

# Harness automatically:
# 1. Clones DevOps/devops-automation
# 2. Places at: /harness/devops-automation/
# 3. Scripts available: devops-automation/scripts/*.py
```

---

### **3. Three-Layer Security**

```
Layer 1: SECRET DETECTION
────────────────────────────
Time: Early (Step 2)
Tool: secret_scan.py
What: Finds hardcoded credentials
Why: Prevents credential leaks
Cost: Low (45 seconds)
Coverage: Pre-commit secrets

Layer 2: STATIC ANALYSIS (SAST)
────────────────────────────────
Time: Middle (Step 6)
Tool: Coverity
What: Analyzes code without running
Why: Finds security bugs (SQL injection, XSS)
Cost: Medium (5 minutes)
Coverage: Application code vulnerabilities

Layer 3: COMPOSITION ANALYSIS (SCA)
────────────────────────────────────
Time: End (Step 7)
Tool: Black Duck
What: Scans third-party dependencies
Why: Finds known CVEs in libraries
Cost: Medium (5 minutes)
Coverage: Supply chain vulnerabilities

Combined Coverage:
✅ Your code (SAST)
✅ Your credentials (Secret Scan)
✅ Your dependencies (SCA)
= 360° Security!
```

**Real-world catch example:**
```
Developer commits code:
├── UserController.java
│   └── Has SQL injection bug (not visible to dev)
├── application.properties
│   └── Has hardcoded password (dev knows but forgot)
└── pom.xml
    └── Uses jackson-databind:2.12.3 (vulnerable, dev doesn't know)

Pipeline catches ALL THREE:
├── Step 2: Finds hardcoded password ✅
├── Step 6: Finds SQL injection ✅
└── Step 7: Finds vulnerable dependency ✅

Result: 3 critical issues caught before production!
```

---

### **4. Fail-Fast Strategy**

**Principle:** Fail as early as possible to save time

```
Order by speed:
├── Step 1: Lint (30s)        ← Fastest, fails early
├── Step 2: Secret (45s)      ← Fast, critical
├── Step 3: Dependencies (2m) ← Moderate
├── Step 4: Build (1.5m)      ← Required for tests
├── Step 5: Tests (45s)       ← Validates logic
├── Step 6: Coverity (5m)     ← Expensive
└── Step 7: Black Duck (5m)   ← Expensive

Why this order?
──────────────
If code style is wrong (lint), why build? (saves 14 mins)
If secrets found, why continue? (security critical)
If build fails, tests can't run (logical dependency)
Run expensive scans only if everything else passes
```

**Time savings:**
```
Bad code style → Fails at 30s (not 15 mins) = 96% time saved
Secret detected → Fails at 1m15s (not 15 mins) = 92% time saved
Build error → Fails at 4m50s (not 15 mins) = 68% time saved
```

---

### **5. Automatic Trigger**

**One trigger, all events:**
```yaml
triggers:
  - trigger:
      type: Webhook
      spec:
        type: Github
        spec:
          type: Any  ← Magic word!
```

**What `type: Any` means:**
```
Catches ALL GitHub events:
✅ Push to any branch
✅ Pull request (opened, updated, reopened)
✅ Merge/close PR
✅ Tag creation
✅ Branch creation

vs. Traditional (3 separate triggers):
❌ Trigger 1: Push events only
❌ Trigger 2: PR events only
❌ Trigger 3: Merge events only
= 3x configuration, 3x maintenance
```

**Event detection:**
```
GitHub sends event type in webhook payload:
{
  "event": "push",
  "branch": "feature/login"
}

Pipeline automatically:
1. Receives event
2. Extracts branch name
3. Uses <+trigger.branch> variable
4. Builds correct branch

No manual configuration needed!
```

---

## 🎬 Demo Script

### **Introduction (2 minutes)**

**Slide 1: Problem Statement**
```
"Today I'll demonstrate our CI/CD pipeline that automates quality 
and security checks for Spring Boot applications.

The problem we solved:
- Before: Manual builds took 2 hours, inconsistent quality checks
- Security issues discovered in production
- No standardized process across teams

Our solution:
- Automated 7-step quality pipeline
- Runs in 15 minutes
- Catches issues before they reach production
- 100% consistent across all projects"
```

---

### **Demo Part 1: Trigger (5 minutes)**

**Live Demo:**

```bash
# Terminal 1: Show current state
cd cicd-app-build-verify
git status
git log --oneline -3

# Terminal 2: Open Harness dashboard
# Show: No running pipelines

# Make a simple code change
echo "// Demo change" >> src/main/java/DemoApplication.java

git add .
git commit -m "Demo: Trigger pipeline"
git push origin main
```

**What to highlight:**
```
1. Show git push command
2. Switch to Harness immediately
3. Show: Pipeline auto-starts within 5 seconds
4. Explain: "GitHub webhook triggered this automatically"
5. Show: Pipeline variables (triggerType, branch)
```

---

### **Demo Part 2: Pipeline Execution (8 minutes)**

**For each step, explain:**

```
Step 1: Lint
──────────
Screen: Show step running
Say: "Checks code quality - naming, style, line length"
Show: Real-time logs
Result: ✅ Passed in 30 seconds

Step 2: Secret Scan
───────────────────
Screen: Show step running
Say: "Scans for hardcoded passwords, API keys"
Demo: "If I had committed a password, pipeline would stop here"
Show: Example pattern detection
Result: ✅ No secrets found

Step 3: Dependencies
────────────────────
Screen: Show Maven downloading
Say: "Downloads 88 components from JFrog, 152 MB total"
Explain: "Uses cached dependencies from previous runs"
Result: ✅ All dependencies resolved

Step 4: Build
─────────────
Screen: Show compilation
Say: "Compiles 47 Java files, creates executable JAR"
Show: "ls -lh target/*.jar" output
Result: ✅ demo-1.0.0.jar created (25.4 MB)

Step 5: Unit Tests
──────────────────
Screen: Show tests running
Say: "Executes 23 JUnit tests, measures 87% code coverage"
Show: Test results (Tests run: 23, Failures: 0)
Explain: "If any test fails, pipeline stops"
Result: ✅ All tests passed

Step 6: Coverity SAST
─────────────────────
Screen: Show analysis running
Say: "Static security analysis - finds SQL injection, XSS"
Explain: "Analyzes code without running it"
Show: Example vulnerability report (if any)
Result: ✅ No critical issues

Step 7: Black Duck SCA
──────────────────────
Screen: Show dependency scan
Say: "Scans 88 components for known CVEs"
Explain: "Checks against NVD database"
Show: Component list and risk assessment
Result: ✅ No high-risk vulnerabilities
```

---

### **Demo Part 3: Results (3 minutes)**

**Show artifacts:**
```
1. Deployable JAR
   Location: target/demo-1.0.0.jar
   Size: 25.4 MB
   Ready for: Deployment to DEV/QA

2. Test Reports
   Location: target/surefire-reports/
   Show: HTML report with test results
   Coverage: 87% (target/site/jacoco/)

3. Security Reports
   Coverity: Link to dashboard
   Black Duck: Component risk view

4. Build Logs
   Full execution trace
   Downloadable for audit
```

---

### **Demo Part 4: Key Features (2 minutes)**

**Highlight differentiators:**

```
1. Smart Build Configuration
   "Automatic triggers work seamlessly,
    but QA can manually test any branch"
   
   Show: Manual run with branch override

2. Centralized Scripts
   "One update to DevOps repo,
    applies to all 50+ projects"
   
   Show: additionalRepositories in YAML

3. Three-Layer Security
   "We catch secrets, code vulnerabilities,
    and dependency issues"
   
   Show: Security step sequence

4. Fail-Fast
   "Lint fails in 30 seconds,
    not 15 minutes"
   
   Show: Step order logic
```

---

## ❓ Q&A Preparation

### **Technical Questions:**

**Q1: How does the webhook trigger work?**
```
A: "GitHub sends HTTP POST to Harness when code is pushed.
    Harness validates the event, matches it to our trigger
    configuration (type: Any), and automatically starts the
    pipeline with the correct branch. The entire process
    takes about 5 seconds from push to pipeline start."
```

**Q2: What happens if a step fails?**
```
A: "Pipeline immediately stops at the failed step. For example,
    if Secret Scan finds a password, the pipeline halts and
    doesn't proceed to build. This saves time and prevents
    bad code from progressing. Developers get an email with
    the failure logs and can fix the issue before re-pushing."
```

**Q3: How do you handle dependencies?**
```
A: "We use Maven with JFrog Artifactory. Step 3 downloads
    all dependencies defined in pom.xml. Harness caches
    these in ~/.m2/repository/, so subsequent runs are faster.
    We download 88 components totaling 152 MB. JFrog provides
    enterprise-approved versions and vulnerability scanning."
```

**Q4: Why use additionalRepositories?**
```
A: "Instead of each project maintaining its own scripts, we
    have one central DevOps repository. All pipelines clone
    this repo and use the same scripts. Update once, it
    applies everywhere. This ensures consistency across 50+
    projects and makes governance easier."
```

**Q5: How long does the pipeline take?**
```
A: "Average 15 minutes:
    - Quick checks (lint, secrets): 2 minutes
    - Build and test: 5 minutes
    - Security scans: 8 minutes
    
    If it fails early (e.g., lint), only 30 seconds wasted.
    Fail-fast strategy saves developer time."
```

**Q6: What about test coverage?**
```
A: "We use JaCoCo to measure code coverage. Currently at 87%.
    The tool instruments bytecode during test execution and
    tracks which lines run. Reports show covered/uncovered
    lines. We aim for 80%+ coverage before production."
```

**Q7: Explain the build configuration.**
```
A: "build: <+input>.default(<+trigger.branch>)
    
    This gives us flexibility:
    - Automatic triggers: Uses GitHub branch automatically
    - Manual runs: Prompts with default, can override
    
    Better than:
    - <+input> alone: Always blocks automation
    - <+trigger.branch> alone: Can't override manually
    
    It's production-ready CI/CD with testing flexibility."
```

**Q8: How do security scans work?**
```
A: "Three layers:
    
    1. Secret Scan (45s):
       Regex patterns find passwords, API keys
       
    2. Coverity SAST (5m):
       Static analysis finds SQL injection, XSS
       Analyzes code without running it
       
    3. Black Duck SCA (5m):
       Checks dependencies against CVE database
       Finds vulnerable libraries
    
    Combined: 360° security coverage."
```

**Q9: Can we run pipeline manually?**
```
A: "Yes! Harness UI → Run button → Enter branch name
    
    Use cases:
    - QA testing specific branch
    - Hotfix validation
    - Re-running failed pipeline
    
    The smart build config supports both automatic
    webhook triggers AND manual runs."
```

**Q10: What's in the JAR file?**
```
A: "Executable Spring Boot JAR:
    - Compiled classes (src/main/java)
    - Resources (application.properties)
    - All dependencies (spring-boot, postgresql, etc.)
    - Embedded Tomcat server
    
    Size: 25.4 MB
    Run: java -jar demo-1.0.0.jar
    
    It's self-contained - no external dependencies needed."
```

---

### **Business Questions:**

**Q1: What's the ROI?**
```
A: "Time savings: 2 hours manual → 15 minutes automated = 87.5% faster
    
    For 50 developers × 10 commits/day:
    - Before: 1,000 hours/day manual work
    - After: 125 hours/day automated
    - Savings: 875 developer hours/day
    
    Plus: Security issues caught early (cheaper to fix)"
```

**Q2: How does this improve quality?**
```
A: "Consistent enforcement:
    - Every commit gets same 7 checks
    - No human error or skipping steps
    - Standards enforced automatically
    
    Result: 
    - 95%+ build success rate
    - Zero security issues in production (from caught issues)
    - Faster code reviews (automated checks done)"
```

**Q3: Can this scale?**
```
A: "Yes:
    - Harness Cloud: Auto-scales compute
    - Runs 50+ parallel pipelines
    - Centralized scripts: Update once, applies everywhere
    - No infrastructure to manage
    
    We've scaled from 5 projects to 50+ with same pipeline."
```

**Q4: What if JFrog or Coverity is down?**
```
A: "Built-in retry logic:
    - Maven retries downloads 3x
    - Timeout settings prevent hanging
    - Failure notifications sent immediately
    
    Fallback:
    - Can switch to Maven Central
    - Skip non-critical scans with approval
    - Manual build process still available"
```

---

### **Demo Failure Scenarios:**

**If pipeline fails during demo:**

```
Option 1: Lint fails
Say: "Great! This shows our quality enforcement.
      See, the code style violation is caught immediately.
      Without this, inconsistent code reaches main branch."
Show: Error message, line number
Action: "In production, developer fixes and re-pushes."

Option 2: Secret detected
Say: "Perfect demo of security in action!
      The pipeline stopped because it found a credential.
      This prevents data breaches."
Show: Secret pattern, file location
Action: "We'd remove the hardcoded secret, use env vars."

Option 3: Test fails
Say: "This is exactly why we have automated testing.
      A failing test means the code change broke existing
      functionality. Better caught here than production!"
Show: Which test failed, assertion error
Action: "Developer investigates, fixes business logic."

Option 4: Build fails
Say: "Build failures are common - missing dependency,
      compilation error. Pipeline catches this immediately."
Show: Maven error message
Action: "Fix pom.xml or code syntax."
```

**If nothing fails (happy path):**
```
Say: "Perfect! All 7 quality gates passed.
      This code is now ready for deployment.
      The JAR artifact can go to DEV environment.
      
      Let me show what happens when something fails..."

Then: Show example failure from previous run logs
```

---

## 🎯 Success Metrics

**Track and share:**

```
Pipeline Performance:
├── Average duration: 15m 32s
├── Success rate: 95%
├── Daily executions: 120
└── Time saved: 875 dev hours/day

Quality Improvements:
├── Code coverage: 87% (target: 80%)
├── Security issues caught: 47 (last quarter)
├── Production incidents: 0 (security-related)
└── Code review time: -40% (automated checks done)

Adoption:
├── Projects using pipeline: 52
├── Developers onboarded: 180
├── Daily commits processed: 600
└── Satisfaction score: 4.7/5
```

---

## 🎓 Key Takeaways

**For the demo, emphasize:**

```
1. Automation
   "Push code → 7 automated checks → Ready to deploy"
   
2. Security
   "Three-layer scanning catches issues before production"
   
3. Consistency
   "Same checks for every commit, every developer"
   
4. Speed
   "15 minutes vs 2 hours manual process"
   
5. Scalability
   "50+ projects, centralized maintenance"
```

---

## 📞 Support & Resources

**During demo:**
- GitHub Repo: github.aepsc.com/cicd-app-build-verify
- Harness Project: https://app.harness.io/...
- Documentation: README.md
- DevOps Scripts: github.aepsc.com/DevOps/devops-automation

**After demo:**
- Questions: your-email@company.com
- Onboarding: Link to wiki
- Slack: #cicd-pipeline-support

---

**Good luck with your demo! 🚀**

Remember:
✅ Keep it simple
✅ Show, don't just tell
✅ Have backup plan for failures
✅ Focus on business value
✅ Be confident - you built something great!
