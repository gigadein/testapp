import numpy as np
import matplotlib.pyplot as plt
import control
import streamlit as st
from io import BytesIO

def main():
    # 전달함수 정의
    G = control.TransferFunction([100], [1, 5, 106])

    # 폐루프 전달함수 계산
    T = G / (1 + G)

    # 시뮬레이션 설정
    t = np.linspace(0, 10, 1000)  # 시간 범위 설정
    t, y = control.step_response(T, T=t)  # unit step 입력에 대한 응답곡선 계산

    # 응답곡선 그리기
    fig1, ax1 = plt.subplots()
    ax1.plot(t, y)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Response')
    ax1.set_title('Step Response')
    ax1.grid(True)

    # 주파수 응답 그리기
    fig2, (ax2, ax3) = plt.subplots(2, 1)
    control.bode_plot(T, dB=True, plot=False)
    mag, phase, omega = control.bode_plot(T, dB=True, plot=False)

    ax2.semilogx(omega, mag)
    ax2.set_xlabel('Frequency [rad/s]')
    ax2.set_ylabel('Magnitude [dB]')
    ax2.set_title('Bode Plot - Magnitude')
    ax2.grid(True)

    ax3.semilogx(omega, phase)
    ax3.set_xlabel('Frequency [rad/s]')
    ax3.set_ylabel('Phase [degrees]')
    ax3.set_title('Bode Plot - Phase')
    ax3.grid(True)

    # 그래프를 이미지로 변환하여 Streamlit에 표시
    fig1_data = fig_to_data(fig1)
    fig2_data = fig_to_data(fig2)

    st.image(fig1_data)
    st.image(fig2_data)

def fig_to_data(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf

if __name__ == '__main__':
    main()
