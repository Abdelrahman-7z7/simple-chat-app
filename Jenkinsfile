pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'simple-chat-app'  // Docker image name
    APP_PORT = '8080'                 // Application port
  }

  stages {
    stage('Build') {
      steps {
        echo 'Building the application...'
        script {
          try {
            sh 'docker build -t ${DOCKER_IMAGE} .'
          } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error "Build failed: ${e.message}"
          }
        }
      }
    }
    stage('Test') {
      steps {
        echo 'Running tests...'

        // Run tests and stop if any of them fails
        script {
          try {
            sh 'python tests/homepage_test.py'
            sh 'python tests/websocket_test.py'
            sh 'python tests/content_test.py'
            sh 'python tests/websocket_timeout_test.py'
          } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error "Test failed: ${e.message}"
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying the application...'
        script {
          try {
            sh "docker run -d -p ${APP_PORT}:80 ${DOCKER_IMAGE}"
          } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error "Deployment failed: ${e.message}"
          }
        }
      }
    }
  }

  post {
    always {
      echo 'Cleaning up...'
      sh 'docker system prune -f'  // Cleanup unused Docker resources after the pipeline runs
    }
    success {
      echo 'Pipeline completed successfully!'
    }
    failure {
      echo 'Pipeline failed, investigate the error logs above.'
    }
  }
}
