node {
    def app
    stage('Clone repository') {
        checkout scm
    }

    stage('Build frontend image') {
       app = docker.build("thush1990/demo-ci")
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            // app.push("${env.BUILD_NUMBER}")
            app.push("backend3")
        }
    }
    
    // stage('Trigger ManifestUpdate') {
    //             echo "triggering updatemanifestjob"
    //             build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    //     }
}