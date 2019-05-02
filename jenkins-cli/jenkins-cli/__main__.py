import sys
import argparse
from jenkins_wrapper import JenkinsWrapper
def main():
    parser = argparse.ArgumentParser('jenkins-cli')
    parser.add_argument('--jobname', help='Enter Job name')
    parser.add_argument('username', help='Enter your name')
    args = parser.parse_args()
    print(args.username)
    print(args.jobname)
    jenkins_wrapper = JenkinsWrapper()
    jenkins_wrapper.getJobs()
main()
