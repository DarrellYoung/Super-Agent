# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 07:14:33 2024

@author: mail4
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
ALPHA = 0.1  # Learning rate for the attack model
BETA = 0.05  # Learning rate for defense
K1 = 1.0     # Impact coefficient of attack
K2 = 1.0     # Base effectiveness of defense
K3 = 0.7     # Effectiveness of AI-driven defenses

# Initial Conditions
A0 = 1.0     # Initial attack capability
D0 = 1.0     # Initial defense effectiveness
S0 = 1.0     # Initial security state

# Time
T = np.linspace(0, 100, 500)  # Simulation time

def event_driven_response(E, C):
    # Simplified model where E is event strength and C is cloud API responsiveness
    return E * C

def ai_predict(E):
    # Predictive model based on current event data
    return ALPHA * np.log(1 + E)

# Enhanced system dynamics with event-driven and AI predictive models
def enhanced_system(t, y):
    A, D, S, E, C = y
    dA_dt = ALPHA * A
    dD_dt = BETA * D
    dS_dt = -K1 * A * S + K2 * D * (1 - S) + K3 * (A * D) + event_driven_response(E, C)
    dE_dt = -E  # Decay of events over time
    dC_dt = 0.1 * (1 - C)  # Simulate some dynamics for Cloud API responsiveness
    return [dA_dt, dD_dt, dS_dt, dE_dt, dC_dt]

# Initial conditions include events (E) and cloud API responsiveness (C)
initial_conditions = [A0, D0, S0, 0.5, 0.5]  # Assume some initial events and moderate API responsiveness

# Solve the enhanced system
enhanced_solution = solve_ivp(enhanced_system, [T[0], T[-1]], initial_conditions, t_eval=T)

# Plotting function for results
def plot_results(t, solution):
    plt.figure(figsize=(12, 8))
    plt.plot(t, solution.y[0], label='Attack Capability (A)')
    plt.plot(t, solution.y[1], label='Defense Effectiveness (D)')
    plt.plot(t, solution.y[2], label='System Security (S)')
    plt.plot(t, solution.y[3], label='Event Strength (E)')
    plt.plot(t, solution.y[4], label='Cloud API Responsiveness (C)')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Simulation of AI-driven Cybersecurity Dynamics')
    plt.legend()
    plt.grid(True)
    plt.show()

# Execute the plot function to visualize the results
plot_results(T, enhanced_solution)
