pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    
    stage('data creation') {
      steps {
        sh 'python3 data_creation.py'
        echo 'Create data'
      }
    }
    
    stage('data_preprocessing') {
      steps {
        sh 'python3 model_preprocessing.py'
        echo 'Data preprocessing'
      }
    }
    
    stage('data_preparation') {
      steps {
        sh 'python3 model_preparation.py'
        echo 'Data training'
      }
    }
    
    stage('model_testing') {
      steps {
        echo 'Prediction'
        sh 'python3 model_testing.py'
      }
    }
  }
}
