pipeline {
    agent any
    environment {
        PACKAGE_NAME = 'count-files'
        PACKAGE_VERSION = '1.0'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }
        stage('Test Script') {
            steps {
                sh 'chmod +x count_files.sh'
                sh 'bash -n count_files.sh'
            }
        }
        stage('Build RPM') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                dnf install -y rpm-build rpmdevtools
                rpmdev-setuptree
                mkdir -p ~/rpmbuild/SOURCES/${PACKAGE_NAME}-${PACKAGE_VERSION}
                cp count_files.sh ~/rpmbuild/SOURCES/${PACKAGE_NAME}-${PACKAGE_VERSION}/
                cd ~/rpmbuild/SOURCES
                tar czvf ${PACKAGE_NAME}-${PACKAGE_VERSION}.tar.gz ${PACKAGE_NAME}-${PACKAGE_VERSION}
                cp ${WORKSPACE}/packaging/rpm/count-files.spec ~/rpmbuild/SPECS/
                rpmbuild -ba ~/rpmbuild/SPECS/count-files.spec
                cp ~/rpmbuild/RPMS/noarch/*.rpm ${WORKSPACE}/
                chmod 666 ${WORKSPACE}/*.rpm
                '''
            }
        }
        stage('Build DEB') {
            agent {
                docker {
                    image 'ubuntu:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                apt-get update
                apt-get install -y build-essential debhelper devscripts
                mkdir -p build/${PACKAGE_NAME}-${PACKAGE_VERSION}
                cp count_files.sh build/${PACKAGE_NAME}-${PACKAGE_VERSION}/
                cp -r packaging/deb/debian build/${PACKAGE_NAME}-${PACKAGE_VERSION}/
                cd build/${PACKAGE_NAME}-${PACKAGE_VERSION}
                dpkg-buildpackage -us -uc -b
                cp ../*.deb ${WORKSPACE}/
                chmod 666 ${WORKSPACE}/*.deb
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.rpm, *.deb'
        }
    }
}
