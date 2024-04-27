# MLOps. Практическое задание №2 (vo_HW)
## Цель задания
В практическом задании по этому модулю вам нужно разработать собственный конвейер автоматизации для проекта машинного обучения. Конвейер должен быть аналогичен тому, который мы рассмотрели в последнем юните этого модуля.

## Содержание задания
Для этого вам понадобится виртуальная машина с установленным Jenkins, python и необходимыми библиотеками. В ходе выполнения практического задания вам необходимо автоматизировать сбор данных, подготовку датасета, обучение модели и работу модели.

## Этапы
- Развернуть сервер с Jenkins, установить необходимое программное обеспечение для работы над созданием модели машинного обучения.
- Выбрать способ получения данных (скачать из github, из интернета, wget, SQL-запрос, …).
- Провести обработку данных, выделить важные признаки, сформировать датасеты для тренировки и тестирования модели, сохранить.
- Создать и обучить на тренировочном датасете модель машинного обучения, сохранить в pickle или аналогичном формате.
- Загрузить сохраненную модель на предыдущем этапе и проанализировать ее качество на тестовых данных.
- Реализовать задания и конвейер. Связать конвейер с системой контроля версий. Сохранить конвейер.


## Решение
- В файле [Jenkins](https://github.com/DanilKhardi/mlops_urfu/blob/main/lab2/Jenkinsfile) реализован конвейер, который настраивает виртуальное окружение, устанваливает необходимые зависимости,последовательно выполняет этапы обучения модели.

![Jenkins](https://github.com/DanilKhardi/mlops_urfu/assets/73106199/34e9a39b-2849-41c9-8ea0-7df0dc83f7f2)

<details>
  <summary><font size="4" color="darkred"><b>Console Output</b></font></summary>
    
  ```bash
  Started by user Danny
  Obtained lab2/Jenkinsfile from git https://github.com/DanilKhardi/mlops_urfu.git
  [Pipeline] Start of Pipeline
  [Pipeline] node
  Running on Jenkins in /var/lib/jenkins/workspace/Lab_2
  [Pipeline] {
  [Pipeline] stage
  [Pipeline] { (Declarative: Checkout SCM)
  [Pipeline] checkout
  Selected Git installation does not exist. Using Default
  The recommended git tool is: NONE
  No credentials specified
  Cloning the remote Git repository
  Cloning repository https://github.com/DanilKhardi/mlops_urfu.git
   > git init /var/lib/jenkins/workspace/Lab_2 # timeout=10
  Fetching upstream changes from https://github.com/DanilKhardi/mlops_urfu.git
   > git --version # timeout=10
   > git --version # 'git version 2.34.1'
   > git fetch --tags --force --progress -- https://github.com/DanilKhardi/mlops_urfu.git +refs/heads/*:refs/remotes/origin/* # timeout=10
   > git config remote.origin.url https://github.com/DanilKhardi/mlops_urfu.git # timeout=10
   > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
  Avoid second fetch
   > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
  Checking out Revision f564fe1ab43c11ef7a13b31b4572193c7da700fd (refs/remotes/origin/main)
   > git config core.sparsecheckout # timeout=10
   > git checkout -f f564fe1ab43c11ef7a13b31b4572193c7da700fd # timeout=10
  Commit message: "Update README.md"
  First time build. Skipping changelog.
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] withEnv
  [Pipeline] {
  [Pipeline] withEnv
  [Pipeline] {
  [Pipeline] stage
  [Pipeline] { (Setup Environment)
  [Pipeline] sh
  + virtualenv .venv
  created virtual environment CPython3.10.12.final.0-64 in 232ms
    creator CPython3Posix(dest=/var/lib/jenkins/workspace/Lab_2/.venv, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/var/lib/jenkins/.local/share/virtualenv)
      added seed packages: pip==22.0.2, setuptools==59.6.0, wheel==0.37.1
    activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
  + . .venv/bin/activate
  + [  = /var/lib/jenkins/workspace/Lab_2@tmp/durable-c47931a9/script.sh.copy ]
  + deactivate nondestructive
  + unset -f pydoc
  + [ -z  ]
  + [ -z  ]
  + hash -r
  + [ -z  ]
  + unset VIRTUAL_ENV
  + [ ! nondestructive = nondestructive ]
  + VIRTUAL_ENV=/var/lib/jenkins/workspace/Lab_2/.venv
  + [  = cygwin ]
  + [  = msys ]
  + export VIRTUAL_ENV
  + _OLD_VIRTUAL_PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
  + PATH=/var/lib/jenkins/workspace/Lab_2/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
  + export PATH
  + [ -z  ]
  + [ -z  ]
  + _OLD_VIRTUAL_PS1=$ 
  + [ x != x ]
  + basename /var/lib/jenkins/workspace/Lab_2/.venv
  + PS1=(.venv) $ 
  + export PS1
  + alias pydoc
  + true
  + hash -r
  + pip install -r lab2/requirements.txt
  Collecting joblib==1.4.0
    Using cached joblib-1.4.0-py3-none-any.whl (301 kB)
  Collecting matplotlib==3.8.4
    Using cached matplotlib-3.8.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
  Collecting numpy==1.26.4
    Using cached numpy-1.26.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)
  Collecting pandas
    Using cached pandas-2.2.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)
  Collecting python-dateutil==2.9.0.post0
    Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
  Collecting scikit-learn
    Using cached scikit_learn-1.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.1 MB)
  Collecting scipy
    Using cached scipy-1.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (38.6 MB)
  Collecting pyparsing>=2.3.1
    Using cached pyparsing-3.1.2-py3-none-any.whl (103 kB)
  Collecting contourpy>=1.0.1
    Using cached contourpy-1.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (305 kB)
  Collecting packaging>=20.0
    Using cached packaging-24.0-py3-none-any.whl (53 kB)
  Collecting kiwisolver>=1.3.1
    Using cached kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
  Collecting fonttools>=4.22.0
    Using cached fonttools-4.51.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
  Collecting pillow>=8
    Using cached pillow-10.3.0-cp310-cp310-manylinux_2_28_x86_64.whl (4.5 MB)
  Collecting cycler>=0.10
    Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
  Collecting six>=1.5
    Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
  Collecting tzdata>=2022.7
    Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
  Collecting pytz>=2020.1
    Using cached pytz-2024.1-py2.py3-none-any.whl (505 kB)
  Collecting threadpoolctl>=2.0.0
    Using cached threadpoolctl-3.4.0-py3-none-any.whl (17 kB)
  Installing collected packages: pytz, tzdata, threadpoolctl, six, pyparsing, pillow, packaging, numpy, kiwisolver, joblib, fonttools, cycler, scipy, python-dateutil, contourpy, scikit-learn, pandas, matplotlib
  Successfully installed contourpy-1.2.1 cycler-0.12.1 fonttools-4.51.0 joblib-1.4.0 kiwisolver-1.4.5 matplotlib-3.8.4 numpy-1.26.4 packaging-24.0 pandas-2.2.2 pillow-10.3.0 pyparsing-3.1.2 python-dateutil-2.9.0.post0 pytz-2024.1 scikit-learn-1.4.2 scipy-1.13.0 six-1.16.0 threadpoolctl-3.4.0 tzdata-2024.1
  + echo OK
  OK
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] stage
  [Pipeline] { (Generate data)
  [Pipeline] echo
  Start generate data
  [Pipeline] sh
  + ./.venv/bin/python3 lab2/data_creation.py
  [Pipeline] echo
  OK
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] stage
  [Pipeline] { (Preprocess model)
  [Pipeline] echo
  Start preprocessing model
  [Pipeline] sh
  + ./.venv/bin/python3 lab2/model_preprocessing.py
  [Pipeline] echo
  OK
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] stage
  [Pipeline] { (Preparation model)
  [Pipeline] echo
  Start preparation model
  [Pipeline] sh
  + ./.venv/bin/python3 lab2/model_preparation.py
  [Pipeline] echo
  OK
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] stage
  [Pipeline] { (Test model)
  [Pipeline] echo
  Start test model
  [Pipeline] sh
  + ./.venv/bin/python3 lab2/model_testing.py
  Mean Squared Error for the test set: 0.027485860976731724
  [Pipeline] echo
  OK
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] stage
  [Pipeline] { (Declarative: Post Actions)
  [Pipeline] echo
  Pipelne done
  [Pipeline] }
  [Pipeline] // stage
  [Pipeline] }
  [Pipeline] // withEnv
  [Pipeline] }
  [Pipeline] // withEnv
  [Pipeline] }
  [Pipeline] // node
  [Pipeline] End of Pipeline
  Finished: SUCCESS
  ```
</details>
