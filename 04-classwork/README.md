# 04-classwork: APIs and Jupyter and git

[donow-answers.md](https://github.com/ilenapeng/foundations/blob/main/04-classwork/donow-answers.md) - Setting up Jupyter notebook, using API keys

[for-loops.ipynb](https://github.com/ilenapeng/foundations/blob/main/04-classwork/for-loops.ipynb) - Notes on using Jupyter notebooks & for loops

[pokemon-api-answers.ipynb](https://github.com/ilenapeng/foundations/blob/main/04-classwork/pokemon-api-answers.ipynb) - Answers to PokéAPI homework from class 3

### More notes from our discussion about [for-loops.ipynb](https://github.com/ilenapeng/foundations/blob/main/04-classwork/for-loops.ipynb) on using Jupyter notebooks & for loops:
* Module not found means you need to run pip install
* ! (bang) in Jupyter notebook means run this in the terminal (i.e, ```!pip install pandas```)
* !! (bang bang) in Terminal means run the above text again, so if you type a file path without cd, the second time do ```cd !!``` and it’ll run
* pip install is for Python and npm (node package manager) installs for Javascript
* git is not the same as GitHub
   * git is the software on your computer that lets you communicate with GitHub
   * git is run from the command line
* Instead of for city in range(len(cities)), you can also just do indices = [0, 1, 2] and then do for index in indices: print(cities[index][‘name’])
* If you’re talking about your list inside of a for loop, youre doing something wrong. if you’re doing a for loop in data[‘abilities’] and you are printing (data[‘abilities’]), then you’re doing it wrong
* import only applies to your current Python file
