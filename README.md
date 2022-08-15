This repository is part of investigation on how to pass variable from some external command or env variable to every Pytest test in a suite

The setup uses as SUT jar of API Challenges by Alan Richardson AKA Evil Tester. 

The jar itself taken from https://github.com/eviltester/thingifier/releases , the explanations about it could be found at https://www.eviltester.com/page/tools/apichallenges/

At present it runs with a variable *baseurl*, set as default in conftest.py under 'test' folder. 

I was able to run test  with Python 3.9 and Pycharm.  