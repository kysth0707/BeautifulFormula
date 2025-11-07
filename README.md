# BeautifulFormula
$$\text{Approximation to a number in }\mathbb{R}\text{ by only using a variable in }\mathbb{R}.$$   

$$\text{This project is using }\LaTeX.$$   
$$\text{You can check if it works on the Online }\LaTeX\text{ Equation Editor.}$$   
https://latexeditor.lagrida.com/

# Test Images ( 3.25 by using t )
<img width="2106" height="503" alt="Image" src="https://github.com/user-attachments/assets/9f4af46e-06e7-4ad9-ad0b-ed44e5f722ab" />
<img width="2157" height="358" alt="Image" src="https://github.com/user-attachments/assets/88ad18c0-8572-4890-a5e8-f297af7d680f" />

# Abstract Rules
1. All terms must be connected by multiplication.
2. You must use only one variable (in Real Number Set)
3. Anyway, make it COOOOOL!
# You can use ...
1. Multiply, Division 
- $$ab,\frac{a}{b}$$
2. Summation, Integral, Product, Factorial
- $$\sum_{a}^{b}c,\int_{a}^{b}c,\prod_{a}^{b}c,\a!$$
3. Subscript, Exponent
- $$a_{b}, a^{b}$$
- So, it's possible to use infinite variable by using subscript!
# Formula
$$\frac{t}{t}=1$$
$$\int_{-\frac{t}{t}}^{\frac{t}{t}}dt_{t}=2$$
$$\sum_{t_{tt}=\frac{t}{t}}^{\int_{-\frac{t}{t}}^{\frac{t}{t}}dt_{t}}t_{tt}=1+2=3$$
$$\int_{-\frac{t}{t}}^{\frac{t}{t}}\int_{-\frac{t}{t}}^{\frac{t}{t}}dt_{t}dt_{tt}=2^{2}=4$$
$$\prod_{t=\frac{t}{t}}^{x}t=x!$$
$$\left( \sum_{t_{t}=\frac{t}{t}}^{x}t_{t} \right)\frac{\int_{-\frac{t}{t}}^{\frac{t}{t}}dt_{t}}{x}=\frac{x(x+1)}{2}\frac{2}{x}=x+1$$
$$\int_{\frac{t}{t}}^{x}t_{t}^{-\frac{t}{t}}dt_{t}=\ln x$$
$$\ln \frac{t}{t}=\int_{\frac{t}{t}}^{\frac{t}{t}}dt_{t}=0$$
$$\sum_{t_{ttt}=\ln \frac{t}{t}}^{\int_{-\frac{t}{t}}^{\frac{t}{t}}\int_{-\frac{t}{t}}^{\frac{t}{t}}dt_{t}dt_{tt}}\frac{x^{t_{ttt}}}{t_{ttt}!}=\sum_{n=0}^{4}\frac{x^{n}}{n!}\approx e^{x}$$
$$a+b=\ln e^{a} + \ln e^{b}=\ln(e^{a}e^{b})$$
$$a+b+\cdots +z=\ln e^{a} + \ln e^{b} + \cdots + \ln e^{z}=\ln(e^{a}e^{b}\cdots e^{z})$$
$$a-b=\ln e^{a} - \ln e^{b}=\ln(\frac{e^{a}}{e^{b}})$$
# The IDEA
- Change target number to bits and approximate number.   
$$2^{1}+2^{0}+2^{-3}=3.125$$
$$=\ln(e^{2^{1}}e^{2^{0}}e^{2^{-3}})\approx \pi$$
- make number (in Natural Number Set) using bits like recursive call.
$$9=2^3+2^0=2^{2^1+2^0}+2^0$$
# Test Images 2
1. e to pi (Go to e_to_pi.ipynb)
2. pi to e (Go to pi_to_e.ipynb)