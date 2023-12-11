# README
## RR(RealRetargeting) 프로젝트 소개
● 이 프로젝트는 실제 영상 및 비디오의 인물 포즈를 추정하여 원하는 캐릭터에 3D Pose를 리타겟팅 시키는 프로젝트입니다.

● ROMP(Pose Estimation) 모델과 Blender, Unreal Engine5를 병합하여 설계한 프로젝트입니다.

<br/><br/>

## RR(RealRetargeting) 프로젝트 설계 배경
● 현재 캐릭터의 애니메이션을 만들기 위해서는 각 프레임마다 캐릭터의 joint들을 조정하고 수정하는 작업을 거쳐 제작하고 있습니다. 이는 자연스러운 애니메이션 생성에는 효과적이나 시간 절약면에서는 효율적이지 못합니다. 

<br/>

● 따라서 저희는 캐릭터 애니메이션을 효과적으로 생성하기 더불어 시간 절약을 위한 방법들을 연구하고자 RR(RealRetargeting)프로젝트를 설계하게 됐습니다.

<br/><br/>
## 환경 설정
### ● Anaconda 및 Miniconda 설치
ROMP 모델(3D Pose Estimation)을 사용하기 위해 가상환경을 구축하여 실험을 진행해야 합니다.

ROMP 모델이 사용하는 패키지가 많기 때문에 올려놓은 Bev.yaml 을 이용하여 가상환경을 구축하면 됩니다.

```
conda env create -f bev.yaml
```

-f 이후에는 파일경로를 입력해주시면 됩니다. ex) -f /choyonggyu/RealRetargeting bev.yaml

가상환경 생성이 끝나게 되면 아래와 같은 코드를 작성하여 활성화를 합니다.

```
conda activate bev
```
<br/>

사용하고 있는 ROMP 모델의 저작권은 아래와 같습니다.
#### ROMP(https://github.com/Arthur151/ROMP)


<br/>

### ● Unreal Engine5 및 Blender 설치
추출한 3D Pose를 리타겟팅 시키기 위해서는 Unreal Engine5 혹은 Blender 중 원하는 프로그램을 다운받아 진행합니다. (각 프로그램마다 3D Pose를 리타겟팅 시키는 방법은 상이합니다.

<br/>

## 방법론
![image](https://github.com/justin0701/RealRetargeting/assets/150767800/f630319e-a931-4fc3-b5cb-a6deb3c6fc47)

#### (Input) 원하는 모션의 영상 및 사진을 촬영하여 Pose 데이터 셋을 준비합니다

#### (1) 준비된 영상 및 사진을 ROMP 내의 Bev(Pose Estimation) 모델에 넣어 3D Pose를 추출합니다. (BVH 형태)

#### (2) 추출된 BVH 형태의 3D Pose를 git에 올라온 convert_bvh_fbx.py 를 사용하여 fbx 형태로 3D Pose를 재 추출합니다.

#### (3) fbx 형태로 추출된 3D Pose를 Unreal Engine 혹은 Blender에서 import 해, 각 프로그램에 맞게 원하는 캐릭터에 리타겟팅을 진행합니다.

#### (Output) 리타겟팅이 완료된 캐릭터를 fbx 형태로 추출하여 원하는 형태에 맞게 이용하면 됩니다.

<br/>
<br/>
<br/>

## 프로젝트 과정 
#### 1. INPUT
<img src="https://github.com/justin0701/RealRetargeting/assets/150767800/716a2b03-835d-4958-b8d7-941b2532089e.png" width="400" height="600">
<br/>
<br/>
위 사진과 같이, 캐릭터에 입히고 싶은 동작을 사진(jpg) 혹은 영상(mp4) 파일로 직접 촬영하여 준비합니다.

#### 2. BEV 이용

bev.yaml을 사용하여 가상환경이 구축이 됐으면 아래 링크에서 안내하는 대로, SMPL 모델을 다운받아 경로에 맞게 저장해줍니다.
https://github.com/Arthur151/ROMP/blob/master/simple_romp/README.md

후에 ROMP 디렉토리에 접근 후 아래 코드를 실행하여 image를 Bev 모델 안에 넣습니다.

```
bev -i /path/to/image.jpg -o /path/to/results.jpg
```

이때 path는
<br/> <br/>
## Acknowledgments
저희의 프로젝트는 ROMP 모델을 수정하고 인용하여 제작되었습니다. 
<br/> <br/>
출처: ROMP(https://github.com/Arthur151/ROMP)









