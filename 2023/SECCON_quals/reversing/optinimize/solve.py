import tqdm


def solve(x):
    import numpy as np

    MOD = x

    def fft_convolve(f, g):
        """
        数列 (多項式) f, g の畳み込みの計算．上下 15 bitずつ分けて計算することで，
        30 bit以下の整数，長さ 250000 程度の数列での計算が正確に行える．
        """
        Lf, Lg = f.shape[-1], g.shape[-1]
        L = Lf + Lg - 1
        fft_len = 1 << L.bit_length()
        fh, fl = f >> 15, f & (1 << 15) - 1
        gh, gl = g >> 15, g & (1 << 15) - 1

        def conv(f, g):
            Ff = np.fft.rfft(f, fft_len)
            Fg = np.fft.rfft(g, fft_len)
            h = np.fft.irfft(Ff * Fg)
            return np.rint(h)[..., :L].astype(np.int64) % MOD

        x = conv(fl, gl)
        z = conv(fh, gh)
        y = conv(fl + fh, gl + gh) - x - z
        return (x + (y << 15) + (z << 30)) % MOD

    def coef_of_generating_function(P, Q, N):
        """compute the coefficient [x^N] P/Q of rational power series.

        Parameters
        ----------
        P : np.ndarray
            Numerator.
        Q : np.ndarray
            Denominator
            Q[0] == 1 and len(Q) == len(P) + 1 is assumed.
        N : int
            The coefficient to compute.
        """
        assert Q[0] == 1 and len(Q) == len(P) + 1

        def convolve(f, g):
            return fft_convolve(f, g)

        while N:
            Q1 = np.empty_like(Q)
            Q1[::2] = Q[::2]
            Q1[1::2] = MOD - Q[1::2]
            P = convolve(P, Q1)[N & 1 :: 2]
            Q = convolve(Q, Q1)[::2]
            N >>= 1
        return P[0]

    def pow_poly(f, n):
        g = [1]
        for i in range(n):
            g = np.convolve(g, f)
        return g

    # ここに表示したい多項式を入力。
    # example: (x^5) / (1-x)^6
    f = pow_poly([3, 0, -1], 1) % MOD
    g = pow_poly([1, 0, -1, -1], 1) % MOD

    # # find_generationg_function.pyで生成したやつを貼り付ける場合はこんな感じ
    # f = [12, 66, 118, 26, -162, -216, -176, -168]
    # g = [1, 3, -1, -10, -5, 8, 6, 0, 0]
    # f = np.array(f) % MOD
    # g = np.array(g) % MOD

    # len(f) + 1 == len(g) になるように調整
    if len(f) >= len(g):
        pad_width = len(f) - len(g) + 1
        g = np.pad(g, (0, pad_width))
    else:
        pad_width = len(g) - len(f) - 1
        f = np.pad(f, (0, pad_width))
    return coef_of_generating_function(f, g, x)


for i in tqdm.trange(2, 1000000):
    solve(i)
