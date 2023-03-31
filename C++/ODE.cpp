#include <iostream>
#include <cmath>

using namespace std;

double f(double x, double y) {
    return x * x + y * y;//y'(x)=f(x,y),这里就是f(x,y)d的表达式
}

int main() {
    double x0, y0, h, xn;
    cout << "Enter initial values: ";
    cin >> x0 >> y0;
    cout << "Enter step size: ";
    cin >> h;
    cout << "Enter final value of x: ";
    cin >> xn;

    int n = (xn - x0) / h;
    double x = x0, y = y0;
    for (int i = 0; i < n; i++) {
        double k1 = h * f(x, y);
        double k2 = h * f(x + h / 2, y + k1 / 2);
        double k3 = h * f(x + h / 2, y + k2 / 2);
        double k4 = h * f(x + h, y + k3);
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        x += h;
    }

    cout << "The numerical solution is: " << y << endl;
    return 0;
}
// 这段代码是一个常见的Runge-Kutta方法的实现，用于求解常微分方程的数值解。
//该方法是一种迭代方法，通过不断迭代来逼近微分方程的解。
//具体来说，该方法将微分方程的解看作是一个函数y(x)，然后通过一系列的计算来逼近这个函数在某些点上的值。
//在这段代码中，我们通过输入初始值x0和y0，步长h以及最终的x值xn，来计算微分方程在x=xn时的数值解。
//具体来说，我们首先计算出迭代次数n，然后在每次迭代中，根据当前的x和y值，计算出四个k值，然后根据这四个k值来更新y值和x值。
//最终，当x=xn时，我们得到的y值就是微分方程在x=xn时的数值解。
// 在具体的实现中，我们定义了一个函数f(x,y)，用于计算微分方程右侧的函数值。
//然后在每次迭代中，我们根据当前的x和y值，计算出四个k值，然后根据这四个k值来更新y值和x值。
//具体来说，我们首先计算出k1=hf(x,y)，然后计算出k2=hf(x+h/2,y+k1/2)，k3=hf(x+h/2,y+k2/2)，k4=hf(x+h,y+k3)，
//最后根据这四个k值来更新y值和x值。具体来说，我们有y+=(k1+2k2+2k3+k4)/6，x+=h。
//最终，当x=xn时，我们得到的y值就是微分方程在x=xn时的数值解。
// 因此，这段代码的原理就是通过Runge-Kutta方法来求解常微分方程的数值解。