pipeline {

    agent any

    stages {

        stage("Checkout From SCM") {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: 'mastert']], browser: [$class: 'GithubWeb', repoUrl: 'https://github.com/moishi-rand/WorldOfTheGames'], extensions: [[$class: 'CloneOption', honorRefspec: true, noTags: true, reference: '', shallow: false], [$class: 'GitLFSPull'], [$class: 'LocalBranch', localBranch: 'mastert']], userRemoteConfigs: [[url: 'https://github.com/moishi-rand/WorldOfTheGames.git']]])
                    }
                }
            }

		stage("Build a docker image") {
            steps {
                script {
                    if (isUnix()==true) {
						sh "docker-compose build"
					}
					else {
						bat "docker-compose build"
					}
					echo "Docker build complete"
                }
            }
        }

		stage("Run docker image") {
            steps {
                script {
                    if (isUnix()==true) {
						sh "docker-compose up -d"
					}
					else {
						bat "docker-compose up -d"
                    }
                    echo "Docker Container is running! Flask online."
					docker_run_check = 1
                }
            }

		stage("Test e2e") {
            steps {
                script {
                    if (isUnix()==true) {
						sh "pip install selenium"
						sh "python3 Tests//e2e.py"

					}
					else {
						bat "pip install selenium"
						bat "cd Tests"
						bat "python Tests//e2e.py"
					}
                }
            }
        }

		stage("Terminate and push image") {
            steps {
                script {
                    if (isUnix()==true){
                        sh 'docker-compose stop'
                        sh 'docker push randmeb/world_of_the_games:WorldOfTheGames'
                    }
                    else{
                        bat 'docker-compose stop'
                        bat 'docker push randmeb/world_of_the_games:WorldOfTheGames'
                        }
                    }
                }
            }
        }
    }
}