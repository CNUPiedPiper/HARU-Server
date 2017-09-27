
Haru(Humanic Awareness and Response Unit) 
===============================================================================

<p align="center">
  <img src="http://i.imgur.com/0TUUXZO.png">
</p>

## Server Version
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

## Introduction
HARU는 라즈베리파이를 이용한 한국어 음성인식 비서 서비스 플랫폼입니다.</br>
해당 Repository는 서버 버전으로 [HARU-Interface](https://github.com/CNUPiedPiper/HARU-Interface)와 함께 동작합니다. Mac OS X 혹은 Linux 환경 위에서 수행할 수 있습니다.

**Haru** is an intelligent personal assistant that can perform tasks or services for an individual especially for Korean with Raspberry PI. This repository is server version, so that it works with [HARU-Interface](https://github.com/CNUPiedPiper/HARU-Interface).</br>
It can be run on Mac OS X or Linux environment.


## Setup
Clone this project with --depth=1 option.
```
$ git clone --depth=1 https://github.com/CNUPiedPiper/HARU-Server.git
```

### Install Dependencies

1. pip가 설치되어 있지 않다면 [pip](https://pip.pypa.io/)를 설치합니다.</br>
Install [pip](https://pip.pypa.io/) if you do not already have them.

2. Python library dependency 충돌 방지를 위해 [virtualenv](https://virtualenv.pypa.io/) 위에서 해당 프로젝트를 수행할 것을 추천합니다. virtualenv는 다음과 같이 설치할 수 있습니다.</br>
We recommend to run this project above from [virtualenv](https://virtualenv.pypa.io/) to avoid dependency conflicts. You can install virtualenv as follows:

```
#In HARU-Server repository
$ sudo pip install virtualenv
```
&nbsp;&nbsp;&nbsp;or if you use ubuntu
```
$ sudo apt-get install python-virtualenv
```

3. virtualenv가 설치되었다면, 다음과 같이 작업합니다.</br>
If virtualenv is installed, do the following:

```
$ virtualenv venv
```

4. 이제 해당 프로젝트에서 작업하고 싶을 때마다 virtualenv를 통해 실행환경을 활성화 시킬 수 있습니다. 실행 방법은 다음과 같습니다.
Now you can activate the execution environment via virtualenv whenever you want to work on that project. Here's how to do it:

```
$ . venv/bin/activate
```

5. Set up shell을 설치합니다. 해당 프로젝트는 Python 2.X.에서 동작합니다.</br>
Install set up shell. It is compatible with Python 2.X.
    
```
$ sh ./setup.sh
```

## This is our demo video !
[![Watch this demo video](https://img.youtube.com/vi/CyqrgM0Fyvk/0.jpg)](https://www.youtube.com/watch?v=CyqrgM0Fyvk)
