def result
def output

pipeline {
  agent any
    stages {
      stage("Illegal Check") {
        steps {
          script {
           echo "Illegal Checking...";
           def scmVars = checkout scm
           println "last successful commit: ${scmVars.GIT_PREVIOUS_SUCCESSFUL_COMMIT}"

           output = sh(returnStdout: true, script: 'pwd')
           println "pwd output = ${output}"

           sh "rm -rf validation && git clone -b master https://github.com/dezhuzhX/hellojenkins.git validation"
           output = sh(returnStdout: true, script: 'cd validation && git diff HEAD~1 | grep "^[+-]" | tee git_diff')
           println '=========================== cd validation && git diff HEAD~1 | grep "^[+-]" | tee git_diff ==========================='
           println "${output}"
           println "======================================================================================================================"

           result = sh(returnStdout: true, script: 'python3 illegal_check.py validation/git_diff')
           echo "check result: ${result}"
           echo "Illegal Checking...done";

           if (result.equals("[]\n")) {
             echo "Check passed, build now...";
             sh "make"
             currentBuild.result = 'SUCCESS'
           } else {
             echo "Check failed.";
             currentBuild.result = 'FAILURE'
           }

           //sh 'rm -rf validation'
         }
       }
     }
   }
}

