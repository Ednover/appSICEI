
pipeline {
  agent any
  stages {
    stage('Stop containers'){
      steps{
        sh 'sudo docker stop $(sudo docker ps -aq)'
      }
    }
    stage('Clone repository') {
      steps {
        git branch: 'develop', url: 'https://github.com/Ednover/sicei.git'
      }
    }
    stage('Install requirements') {
      steps {
        sh 'pip3 install -r requirements.txt --no-cache-dir'
      }
    }
    stage('Run tests') {
      steps {
        sh 'python3 manage.py test' 
      }
    }
    stage('Build') {
      steps {
        sh "sudo docker build . -t sicei-${env.BRANCH_NAME}:1.0.0-${env.BUILD_NUMBER}"
        sh "sudo docker run -p 8000:8000 sicei-${env.BRANCH_NAME}:1.0.0-${env.BUILD_NUMBER}"
      }
    }
  }
}