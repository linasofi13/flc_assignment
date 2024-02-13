<h1 align="center">
    <tt>> ST0270 Formal Languages and Compilers
Assignment 1 </tt> :chess_pawn:
</h1>

### Names: 
- Lina Sofía Ballesteros Merchán
- Santiago Alvarez Díaz


![image](https://github.com/linasofi13/flc_assignment/assets/103126242/c8136719-8c3c-440a-9b3a-fdc646f93f24)

Development of the proposed activity for the subject of Formal Languages and Compilers. Considering the language L = {x ∈ {0,1}
| x represents a multiple of three in binary} and the DFA that accepts said language, with the support of a Python library, the behavior of the automaton is simulated.

## About
- The program was executed on Windows OS.
- The chosen language was Python.
- The libray used was [Automata](https://caleb531.github.io/automata/) and the class used is [DFA](https://caleb531.github.io/automata/api/fa/class-dfa/) .**The library requires Python 3.8 or newer.**
- The code editor used was Visual Studio Code.
- The convention defined for representing the empty string is the character 'e'.

## Run the program

Follow these instructions to run the program:

1. Clone the project on your machine or download the ZIP file.

    ```bash
    git clone git@github.com:linaballesteros/flc_assignment.git
    ```
2. Go to the project directory (or wherever you stored it).

    ```bash
    cd tarea_1_compi
    ```
  
3. Make sure you have Python 3.8 or newer.
  
    ```bash
    python --version

    ```
4. Install the Automaton library required using `pip`

    ```bash
    pip install automata-lib
    ```

## Run the Program

1. Go to the project directory in your code editor or terminal:
   
    ```bash
     cd tarea_1_compi
    ```

3. Run the following in your command prompt:

    ```bash
    python binary3.py
    ```
    
4. Enter your input, for example:

    ```bash
    Enter your string: 1111 
    ```
5. Check results.
     ```bash
   The DFA accepts the string ’1111’
    ```
