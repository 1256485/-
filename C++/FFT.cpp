#include <iostream>
#include <complex>
#include <cmath>
using namespace std;

const double PI = acos(-1);

void FFT(complex<double>* a, int n, int inv) {
    if (n == 1) return;
    complex<double> a0[n / 2], a1[n / 2];
    for (int i = 0; i < n / 2; i++) {
        a0[i] = a[2 * i];
        a1[i] = a[2 * i + 1];
    }
    FFT(a0, n / 2, inv);
    FFT(a1, n / 2, inv);
    complex<double> wn(cos(2 * PI / n), inv * sin(2 * PI / n)), w(1, 0);
    for (int i = 0; i < n / 2; i++) {
        a[i] = a0[i] + w * a1[i];
        a[i + n / 2] = a0[i] - w * a1[i];
        w *= wn;
    }
}

void FFT(complex<double>* a, int n) {
    FFT(a, n, 1);
}

void IFFT(complex<double>* a, int n) {
    FFT(a, n, -1);
    for (int i = 0; i < n; i++) {
        a[i] /= n;
    }
}

int main() {
    int n = 8;
    complex<double> a[n] = {1, 2, 3, 4, 5, 6, 7, 8};
    FFT(a, n);
    for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
    }
    IFFT(a, n);
    for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
    }
    return 0;
}
