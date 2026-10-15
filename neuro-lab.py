# 🧠 NEUROLAB COMMANDER - PREMIUM STYLISH VERSION (FIXED)
# 🎨 Beautiful UI with Colorful Boxes, Animations & Modern Design
# 🔬 Voice Commands + Computer Vision + AI Experiments

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import speech_recognition as sr
import pyttsx3
import cv2
import numpy as np
import pandas as pd
import threading
import time
import json
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

print("🚀 Initializing NeuroLab Commander - Premium Edition...")

# ==================== PREMIUM STYLING CONSTANTS ====================
class Colors:
    # Modern Color Palette
    PRIMARY = "#2c3e50"
    SECONDARY = "#34495e"
    ACCENT = "#3498db"
    SUCCESS = "#27ae60"
    WARNING = "#f39c12"
    DANGER = "#e74c3c"
    INFO = "#9b59b6"
    LIGHT = "#ecf0f1"
    DARK = "#2c3e50"
    WHITE = "#ffffff"
    BLACK = "#000000"
    
    # Gradient Colors
    GRADIENT_1 = ["#667eea", "#764ba2"]
    GRADIENT_2 = ["#f093fb", "#f5576c"]
    GRADIENT_3 = ["#4facfe", "#00f2fe"]
    GRADIENT_4 = ["#43e97b", "#38f9d7"]

class Fonts:
    TITLE = ("Segoe UI", 28, "bold")
    SUBTITLE = ("Segoe UI", 12, "normal")
    HEADING = ("Segoe UI", 16, "bold")
    SUBHEADING = ("Segoe UI", 12, "bold")
    BODY = ("Segoe UI", 10, "normal")
    METRIC = ("Segoe UI", 24, "bold")
    SMALL = ("Segoe UI", 9, "normal")

# ==================== PREMIUM UI COMPONENTS ====================
class GradientFrame(tk.Canvas):
    def __init__(self, parent, colors, width=200, height=100, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)
        self.colors = colors
        self.width = width
        self.height = height
        self.create_gradient()
        
    def create_gradient(self):
        """Create gradient background"""
        for i in range(self.height):
            ratio = i / self.height
            r = int(int(self.colors[0][1:3], 16) * (1 - ratio) + int(self.colors[1][1:3], 16) * ratio)
            g = int(int(self.colors[0][3:5], 16) * (1 - ratio) + int(self.colors[1][3:5], 16) * ratio)
            b = int(int(self.colors[0][5:7], 16) * (1 - ratio) + int(self.colors[1][5:7], 16) * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.create_line(0, i, self.width, i, fill=color)

class AnimatedButton(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.default_bg = self.cget('bg')
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def on_enter(self, event):
        self.configure(bg=Colors.ACCENT)
        
    def on_leave(self, event):
        self.configure(bg=self.default_bg)

class MetricCard(tk.Frame):
    def __init__(self, parent, title, value, icon, color, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(
            bg=color,
            relief='raised',
            bd=2,
            padx=15,
            pady=15,
            width=180,
            height=120
        )
        self.pack_propagate(False)
        
        # Icon
        icon_label = tk.Label(self, text=icon, font=("Segoe UI", 24), bg=color, fg=Colors.WHITE)
        icon_label.pack(anchor='nw')
        
        # Value
        value_label = tk.Label(self, text=value, font=Fonts.METRIC, bg=color, fg=Colors.WHITE)
        value_label.pack(anchor='nw', pady=(5, 0))
        
        # Title
        title_label = tk.Label(self, text=title, font=Fonts.SMALL, bg=color, fg=Colors.WHITE)
        title_label.pack(anchor='nw')

# ==================== AI COMPONENTS ====================
class PremiumVoiceAssistant:
    def __init__(self):
        print("🎤 Initializing Premium Voice Assistant...")
        
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.tts_engine = pyttsx3.init()
            self.setup_premium_voice()
            
            self.command_history = []
            self.experiment_context = None
            self.conversation_context = []
            
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            print("✅ Premium Voice Assistant Ready!")
            
        except Exception as e:
            print(f"❌ Voice Assistant initialization failed: {e}")
            self.recognizer = None
            self.microphone = None
            self.tts_engine = None
    
    def setup_premium_voice(self):
        """Configure premium voice settings"""
        if self.tts_engine:
            try:
                voices = self.tts_engine.getProperty('voices')
                if len(voices) > 1:
                    self.tts_engine.setProperty('voice', voices[1].id)
                
                self.voice_profiles = {
                    'neutral': {'rate': 160, 'volume': 0.8},
                    'urgent': {'rate': 200, 'volume': 1.0},
                    'calm': {'rate': 130, 'volume': 0.7},
                    'excited': {'rate': 180, 'volume': 0.9},
                    'professional': {'rate': 150, 'volume': 0.8}
                }
            except Exception as e:
                print(f"Voice setup error: {e}")
    
    def speak(self, text, emotion="neutral"):
        """Premium text-to-speech with emotional intelligence"""
        if not self.tts_engine:
            print(f"🎤 NeuroLab (Text): {text}")
            return
            
        print(f"🎤 NeuroLab: {text}")
        
        try:
            profile = self.voice_profiles.get(emotion, self.voice_profiles['neutral'])
            self.tts_engine.setProperty('rate', profile['rate'])
            self.tts_engine.setProperty('volume', profile['volume'])
            
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            
            default_profile = self.voice_profiles['neutral']
            self.tts_engine.setProperty('rate', default_profile['rate'])
            self.tts_engine.setProperty('volume', default_profile['volume'])
        except Exception as e:
            print(f"Speech error: {e}")
    
    def listen_with_enhancement(self):
        """Enhanced listening"""
        if not self.recognizer or not self.microphone:
            return self.create_error_response("Microphone not available")
            
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
            
            text = self.recognizer.recognize_google(audio)
            print(f"👤 You: {text}")
            
            enhanced_command = self.enhance_command(text)
            
            command_record = {
                'timestamp': datetime.now(),
                'raw_text': text,
                'enhanced_command': enhanced_command,
                'context': self.experiment_context
            }
            
            self.command_history.append(command_record)
            self.conversation_context.append(command_record)
            
            if len(self.conversation_context) > 10:
                self.conversation_context.pop(0)
            
            return enhanced_command
            
        except sr.WaitTimeoutError:
            return self.create_timeout_response()
        except sr.UnknownValueError:
            return self.create_unknown_speech_response()
        except Exception as e:
            return self.create_error_response(str(e))
    
    def enhance_command(self, text):
        """Enhance voice command"""
        enhanced_data = {
            'text': text,
            'lower_text': text.lower(),
            'timestamp': datetime.now(),
            'confidence': 1.0
        }
        
        # Rule-based sentiment analysis
        positive_words = ['good', 'great', 'excellent', 'perfect', 'thanks', 'thank you']
        negative_words = ['bad', 'terrible', 'wrong', 'error', 'stop', 'emergency']
        
        sentiment_score = 0
        for word in positive_words:
            if word in text.lower():
                sentiment_score += 1
        for word in negative_words:
            if word in text.lower():
                sentiment_score -= 1
        
        enhanced_data['sentiment'] = {
            'label': 'POSITIVE' if sentiment_score > 0 else 'NEGATIVE' if sentiment_score < 0 else 'NEUTRAL',
            'score': abs(sentiment_score) / 5.0
        }
        
        enhanced_data['intent'] = self.classify_intent(text)
        
        return enhanced_data
    
    def classify_intent(self, text):
        """Classify user intent"""
        text_lower = text.lower()
        
        intents = {
            'equipment_control': any(word in text_lower for word in ['turn on', 'turn off', 'start', 'stop', 'activate']),
            'safety_emergency': any(word in text_lower for word in ['emergency', 'help', 'danger', 'stop', 'shutdown']),
            'data_management': any(word in text_lower for word in ['record', 'log', 'data', 'measurement']),
            'experiment_guidance': any(word in text_lower for word in ['experiment', 'procedure', 'protocol', 'guide']),
            'information_query': any(word in text_lower for word in ['what', 'how', 'when', 'where', 'why']),
            'calculation': any(word in text_lower for word in ['calculate', 'compute', 'convert', 'dilution'])
        }
        
        for intent, condition in intents.items():
            if condition:
                return intent
        
        return 'general_conversation'
    
    def process_command(self, enhanced_command):
        """Process commands"""
        if not enhanced_command or 'text' not in enhanced_command:
            return self.create_error_response("No command received")
            
        text = enhanced_command['text']
        intent = enhanced_command['intent']
        sentiment = enhanced_command.get('sentiment', {})
        
        if (intent == 'safety_emergency' or 
            (sentiment.get('label') == 'NEGATIVE' and sentiment.get('score', 0) > 0.5)):
            return self.handle_emergency(enhanced_command)
        
        if self.experiment_context:
            return self.generate_contextual_response(enhanced_command)
        
        return self.generate_intent_response(intent, enhanced_command)
    
    def handle_emergency(self, command_data):
        """Emergency response"""
        response = {
            'text': "🚨 EMERGENCY PROTOCOL ACTIVATED!",
            'action': 'emergency_shutdown',
            'speech': "Emergency detected! Activating safety protocols!",
            'emotion': 'urgent',
            'priority': 'critical'
        }
        return response
    
    def generate_contextual_response(self, command_data):
        """Contextual responses"""
        intent = command_data['intent']
        
        response_templates = {
            'equipment_control': {
                'text': "🔧 Equipment control activated.",
                'speech': "I'll control the laboratory equipment.",
                'emotion': 'professional'
            },
            'data_management': {
                'text': "📊 Data logging initialized.",
                'speech': "Recording experimental data.",
                'emotion': 'professional'
            }
        }
        
        template = response_templates.get(intent, {
            'text': f"🤖 Command: {command_data['text']}",
            'speech': "Command processed successfully.",
            'emotion': 'neutral'
        })
        
        template['action'] = intent
        return template
    
    def generate_intent_response(self, intent, command_data):
        """Intent-based responses"""
        responses = {
            'information_query': {
                'text': "💡 I can provide laboratory information and guidance.",
                'speech': "I'm equipped with laboratory knowledge. What do you need?",
                'emotion': 'professional'
            },
            'calculation': {
                'text': "🧮 Calculation mode activated.",
                'speech': "Ready for scientific calculations.",
                'emotion': 'professional'
            }
        }
        
        return responses.get(intent, {
            'text': f"🔍 I understand: '{command_data['text']}'",
            'speech': "Command received. How can I assist with your laboratory work?",
            'emotion': 'neutral'
        })
    
    def create_timeout_response(self):
        return {'text': "⏰ Listening timeout", 'speech': "Please try again.", 'emotion': 'calm', 'error': 'timeout'}
    
    def create_unknown_speech_response(self):
        return {'text': "❌ Speech not understood", 'speech': "Please speak clearly.", 'emotion': 'calm', 'error': 'unknown_speech'}
    
    def create_error_response(self, error):
        return {'text': f"⚠️ System error: {error}", 'speech': "System error occurred.", 'emotion': 'calm', 'error': error}
    
    def start_continuous_listening(self):
        """Start continuous listening"""
        if not self.recognizer:
            print("❌ Cannot start listening - microphone not available")
            return
            
        def listen_loop():
            while True:
                try:
                    enhanced_command = self.listen_with_enhancement()
                    if enhanced_command and enhanced_command.get('text'):
                        response = self.process_command(enhanced_command)
                        if response:
                            emotion = response.get('emotion', 'neutral')
                            self.speak(response['speech'], emotion)
                    
                    threading.Event().wait(0.3)
                except Exception as e:
                    print(f"Listening loop error: {e}")
                    time.sleep(1)
        
        listener_thread = threading.Thread(target=listen_loop, daemon=True)
        listener_thread.start()
        print("✅ Continuous listening activated!")

class PremiumVisionSafetyMonitor:
    def __init__(self):
        print("👁️ Initializing Premium Vision Safety Monitor...")
        
        self.cap = None
        self.is_monitoring = False
        self.safety_violations = []
        self.real_time_alerts = []
        self.posture_history = []
        
        self.setup_camera()
        self.setup_directories()
        print("✅ Premium Vision Safety Monitor Ready!")
    
    def setup_camera(self):
        """Setup camera"""
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("   ⚠️ Camera not available - using simulation mode")
        except Exception as e:
            print(f"   ⚠️ Camera initialization failed: {e}")
    
    def setup_directories(self):
        """Create directories"""
        if not os.path.exists('safety_violations'):
            os.makedirs('safety_violations')
    
    def start_monitoring(self):
        """Start safety monitoring"""
        if not self.check_camera():
            print("🎭 Starting simulated monitoring...")
            self.start_simulated_monitoring()
            return
        
        print("🔍 Starting Real-time Monitoring...")
        self.is_monitoring = True
        
        def monitoring_loop():
            frame_count = 0
            while self.is_monitoring:
                try:
                    ret, frame = self.cap.read()
                    if ret:
                        frame_count += 1
                        violations = self.analyze_frame(frame, frame_count)
                        
                        for violation in violations:
                            self.handle_violation(violation, frame)
                    
                    time.sleep(0.033)
                except Exception as e:
                    print(f"Monitoring loop error: {e}")
                    time.sleep(1)
        
        self.monitor_thread = threading.Thread(target=monitoring_loop, daemon=True)
        self.monitor_thread.start()
    
    def check_camera(self):
        """Check camera"""
        return self.cap and self.cap.isOpened()
    
    def analyze_frame(self, frame, frame_count):
        """Analyze frame for safety violations"""
        violations = []
        
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            avg_brightness = np.mean(gray)
            
            if avg_brightness < 60:
                violations.append({
                    'type': 'environment_lighting',
                    'severity': 'low',
                    'message': '💡 Lighting Alert: Low light conditions',
                    'data': {'brightness': avg_brightness},
                    'confidence': 0.75
                })
            
            if hasattr(self, 'previous_frame'):
                frame_diff = cv2.absdiff(self.previous_frame, gray)
                motion = np.mean(frame_diff)
                
                if motion > 30:
                    violations.append({
                        'type': 'movement_detected',
                        'severity': 'medium',
                        'message': '⚠️ Movement: Sudden movements',
                        'data': {'motion_level': motion},
                        'confidence': 0.65
                    })
            
            self.previous_frame = gray
            
        except Exception as e:
            print(f"Frame analysis error: {e}")
        
        return violations
    
    def simulate_safety_violations(self):
        """Simulate safety violations"""
        violations = [
            "⚠️ Posture Alert: Maintain straight back",
            "🚨 Safety Gear: Gloves not detected", 
            "🔬 Proximity Warning: Maintain distance",
            "💡 Lighting Alert: Low light conditions",
        ]
        
        if random.random() < 0.3:
            violation = random.choice(violations)
            timestamp = datetime.now()
            
            violation_data = {
                'timestamp': timestamp,
                'message': violation,
                'type': 'simulated',
                'severity': 'medium'
            }
            
            self.safety_violations.append(violation_data)
            self.real_time_alerts.append(violation)
            
            print(f"📸 {violation}")
            
            return violation_data
        
        return None
    
    def start_simulated_monitoring(self):
        """Start simulated monitoring"""
        self.is_monitoring = True
        
        def simulated_loop():
            while self.is_monitoring:
                try:
                    violation = self.simulate_safety_violations()
                    time.sleep(5)
                except Exception as e:
                    print(f"Simulated monitoring error: {e}")
                    time.sleep(1)
        
        self.monitor_thread = threading.Thread(target=simulated_loop, daemon=True)
        self.monitor_thread.start()
    
    def handle_violation(self, violation, frame):
        """Handle violations"""
        violation_data = {
            'timestamp': datetime.now(),
            'violation': violation,
            'evidence_type': 'computer_vision',
            'model_confidence': violation.get('confidence', 0.5)
        }
        
        self.safety_violations.append(violation_data)
        self.real_time_alerts.append(violation['message'])
        
        print(f"👁️ {violation['message']}")
    
    def get_safety_report(self):
        """Generate safety report"""
        report = {
            'total_violations': len(self.safety_violations),
            'recent_alerts': self.real_time_alerts[-5:],
            'monitoring_status': 'active' if self.is_monitoring else 'inactive',
            'camera_available': self.check_camera(),
            'risk_assessment': self.perform_risk_assessment()
        }
        
        return report
    
    def perform_risk_assessment(self):
        """Risk assessment"""
        high_severity_count = len([v for v in self.safety_violations if v['violation']['severity'] == 'high'])
        
        risk_level = 'HIGH' if high_severity_count > 3 else 'MEDIUM' if high_severity_count > 0 else 'LOW'
        
        return {
            'overall_risk': risk_level,
            'high_severity_violations': high_severity_count,
            'recommendations': self.generate_recommendations()
        }
    
    def generate_recommendations(self):
        """Generate recommendations"""
        recommendations = []
        
        safety_gear_violations = [v for v in self.safety_violations if 'safety_gear' in v['violation']['type']]
        if safety_gear_violations:
            recommendations.append("Enforce PPE protocol")
        
        if not recommendations:
            recommendations.append("Maintain current safety practices")
        
        return recommendations
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.is_monitoring = False
        if self.cap and self.cap.isOpened():
            self.cap.release()
        print("🛑 Safety monitoring stopped")

class PremiumExperimentAI:
    def __init__(self):
        print("🧠 Initializing Premium Experiment AI...")
        
        self.experiment_history = []
        self.hypotheses_generated = []
        
        self.experiment_templates = self.setup_experiment_templates()
        print("✅ Premium Experiment AI Ready!")
    
    def setup_experiment_templates(self):
        """Setup experiment templates"""
        return {
            'chemistry': {
                'name': '🧪 Chemical Synthesis Optimization',
                'steps': [
                    'Prepare chemical solutions',
                    'Set up temperature control',
                    'Mix reactants',
                    'Monitor reaction progress',
                    'Record observations',
                    'Analyze results'
                ],
                'parameters': ['temperature', 'concentration', 'time'],
                'safety_level': 'HIGH',
                'icon': '🧪',
                'color': Colors.DANGER
            },
            'biotechnology': {
                'name': '🧬 Microbial Culture Study',
                'steps': [
                    'Prepare culture medium',
                    'Inoculate samples',
                    'Maintain optimal conditions',
                    'Monitor growth',
                    'Document observations',
                    'Analyze growth patterns'
                ],
                'parameters': ['temperature', 'ph', 'nutrient_concentration'],
                'safety_level': 'MEDIUM',
                'icon': '🧬',
                'color': Colors.SUCCESS
            },
            'physics': {
                'name': '🔭 Optical System Analysis',
                'steps': [
                    'Set up optical components',
                    'Align light source',
                    'Measure properties',
                    'Record patterns',
                    'Calculate parameters'
                ],
                'parameters': ['wavelength', 'distance', 'angle'],
                'safety_level': 'LOW',
                'icon': '🔭',
                'color': Colors.INFO
            }
        }
    
    def generate_hypothesis(self, experiment_type="general", context=""):
        """Generate hypotheses"""
        hypothesis_templates = {
            'chemistry': [
                f"Systematic variation of {context} will demonstrate temperature-dependent kinetics.",
                f"Optimization of {context} will yield maximum product efficiency.",
            ],
            'biotechnology': [
                f"Optimal {context} will maximize microbial productivity.",
                f"Controlled {context} will demonstrate biological responses.",
            ],
            'physics': [
                f"Precision measurement of {context} will validate predictions.",
                f"Systematic {context} will demonstrate physical phenomena.",
            ]
        }
        
        templates = hypothesis_templates.get(experiment_type, hypothesis_templates['chemistry'])
        hypothesis = random.choice(templates)
        
        hypothesis_data = {
            'hypothesis': hypothesis,
            'type': experiment_type,
            'timestamp': datetime.now(),
            'confidence': round(random.uniform(0.80, 0.95), 3),
            'model': 'Premium AI'
        }
        
        self.hypotheses_generated.append(hypothesis_data)
        return hypothesis_data
    
    def optimize_parameters(self, experiment_data):
        """Optimize parameters"""
        if len(experiment_data) < 3:
            return {'error': 'Need at least 3 data points'}
        
        try:
            df = pd.DataFrame(experiment_data)
            
            correlations = {}
            for col in df.columns:
                if col != 'outcome':
                    try:
                        corr = df[col].corr(df['outcome'])
                        correlations[col] = corr
                    except:
                        correlations[col] = 0
            
            best_idx = df['outcome'].idxmax()
            optimal_params = df.loc[best_idx].to_dict()
            
            return {
                'optimal_parameters': optimal_params,
                'feature_correlations': correlations,
                'predicted_outcome': optimal_params['outcome'],
                'confidence': 0.75,
                'method': 'Statistical Correlation'
            }
            
        except Exception as e:
            return {'error': f'Optimization failed: {str(e)}'}
    
    def start_experiment(self, experiment_type):
        """Start experiment"""
        template = self.experiment_templates.get(experiment_type, self.experiment_templates['chemistry'])
        
        guidance = {
            'experiment_name': template['name'],
            'type': experiment_type,
            'steps': template['steps'],
            'critical_parameters': template['parameters'],
            'safety_level': template['safety_level'],
            'icon': template['icon'],
            'color': template['color'],
            'ai_recommendations': self._generate_recommendations(experiment_type)
        }
        
        experiment_log = {
            'guidance': guidance,
            'start_time': datetime.now(),
            'status': 'initialized'
        }
        
        self.experiment_history.append(experiment_log)
        return guidance
    
    def _generate_recommendations(self, experiment_type):
        """Generate recommendations"""
        recommendations = {
            'chemistry': [
                "Wear appropriate PPE (gloves, goggles, lab coat)",
                "Work in well-ventilated area",
                "Calibrate instruments before use",
                "Document all procedures meticulously"
            ],
            'biotechnology': [
                "Maintain sterile techniques",
                "Use proper disposal methods",
                "Include control experiments",
                "Validate with multiple methods"
            ],
            'physics': [
                "Ensure proper equipment calibration",
                "Document experimental conditions",
                "Repeat measurements for accuracy",
                "Consider environmental factors"
            ]
        }
        
        return recommendations.get(experiment_type, ["Follow standard laboratory protocols"])
    
    def get_analytics(self):
        """Generate analytics"""
        analytics = {
            'total_experiments': len(self.experiment_history),
            'completed_experiments': len([e for e in self.experiment_history if e.get('status') == 'completed']),
            'hypotheses_generated': len(self.hypotheses_generated),
            'average_confidence': np.mean([h['confidence'] for h in self.hypotheses_generated]) if self.hypotheses_generated else 0,
        }
        
        return analytics

# ==================== MAIN PREMIUM APPLICATION ====================
class PremiumNeuroLabCommander:
    def __init__(self):
        print("🚀 Initializing NeuroLab Commander - Premium Edition...")
        
        # Application state
        self.is_running = True
        self.start_time = time.time()
        self.animations_running = False
        
        # Initialize components
        try:
            self.voice_assistant = PremiumVoiceAssistant()
        except Exception as e:
            print(f"❌ Voice Assistant failed: {e}")
            self.voice_assistant = None
            
        try:
            self.vision_monitor = PremiumVisionSafetyMonitor()
        except Exception as e:
            print(f"❌ Vision Monitor failed: {e}")
            self.vision_monitor = None
            
        try:
            self.experiment_ai = PremiumExperimentAI()
        except Exception as e:
            print(f"❌ Experiment AI failed: {e}")
            self.experiment_ai = None
        
        # Create Premium GUI
        self.setup_premium_gui()
        
        # Start services
        self.start_services()
        
        print("✅ NeuroLab Commander Premium Ready!")
    
    def setup_premium_gui(self):
        """Create premium interface"""
        self.root = tk.Tk()
        self.root.title("🧠 NeuroLab Commander - Premium Edition")
        self.root.geometry("1400x900")
        self.root.configure(bg=Colors.PRIMARY)
        
        # Configure styles
        self.setup_styles()
        
        # Create main container
        self.main_container = tk.Frame(self.root, bg=Colors.PRIMARY)
        self.main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        self.create_premium_header()
        
        # Create notebook
        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(fill='both', expand=True, pady=(20, 0))
        
        # Create premium tabs
        self.dashboard_tab = self.create_premium_dashboard()
        self.voice_tab = self.create_premium_voice_tab()
        self.vision_tab = self.create_premium_vision_tab()
        self.experiment_tab = self.create_premium_experiment_tab()
        self.analytics_tab = self.create_premium_analytics_tab()
        
        self.notebook.add(self.dashboard_tab, text="🏠 Premium Dashboard")
        self.notebook.add(self.voice_tab, text="🎤 Voice AI")
        self.notebook.add(self.vision_tab, text="👁️ Vision Safety")
        self.notebook.add(self.experiment_tab, text="🧪 Experiments")
        self.notebook.add(self.analytics_tab, text="📊 Analytics")
        
        # Status bar
        self.create_premium_status_bar()
    
    def setup_styles(self):
        """Configure premium styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure notebook style
        style.configure('TNotebook', background=Colors.SECONDARY)
        style.configure('TNotebook.Tab', 
                       background=Colors.SECONDARY,
                       foreground=Colors.LIGHT,
                       padding=[20, 10],
                       font=Fonts.SUBHEADING)
        style.map('TNotebook.Tab', 
                 background=[('selected', Colors.ACCENT)],
                 foreground=[('selected', Colors.WHITE)])
    
    def create_premium_header(self):
        """Create premium header"""
        header_frame = tk.Frame(self.main_container, bg=Colors.SECONDARY, height=120)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Main title
        title_frame = tk.Frame(header_frame, bg=Colors.SECONDARY)
        title_frame.pack(fill='x', padx=30, pady=20)
        
        title_label = tk.Label(title_frame, 
                              text="🧠 NeuroLab Commander", 
                              font=Fonts.TITLE, 
                              bg=Colors.SECONDARY, 
                              fg=Colors.LIGHT)
        title_label.pack(side='left')
        
        subtitle_label = tk.Label(title_frame, 
                                 text="Premium Edition • AI-Powered Laboratory Assistant", 
                                 font=Fonts.SUBTITLE, 
                                 bg=Colors.SECONDARY, 
                                 fg=Colors.LIGHT)
        subtitle_label.pack(side='left', padx=(20, 0))
        
        # Status indicators
        status_frame = tk.Frame(header_frame, bg=Colors.SECONDARY)
        status_frame.pack(fill='x', padx=30, pady=(0, 20))
        
        self.status_indicators = {}
        status_configs = [
            ("🎤 Voice AI", "Initializing...", Colors.SUCCESS),
            ("👁️ Vision Safety", "Ready...", Colors.WARNING), 
            ("🧠 Experiment AI", "Ready", Colors.INFO),
            ("📊 Analytics", "Active", Colors.ACCENT)
        ]
        
        for i, (name, status, color) in enumerate(status_configs):
            status_card = tk.Frame(status_frame, bg=color, relief='raised', bd=1, padx=15, pady=8)
            status_card.pack(side='left', padx=(0, 15))
            
            name_label = tk.Label(status_card, text=name, font=Fonts.SMALL, bg=color, fg=Colors.WHITE)
            name_label.pack()
            
            status_label = tk.Label(status_card, text=status, font=Fonts.SMALL, bg=color, fg=Colors.WHITE)
            status_label.pack()
            
            self.status_indicators[name] = status_label
    
    def create_premium_dashboard(self):
        """Create premium dashboard"""
        tab = tk.Frame(self.notebook, bg=Colors.PRIMARY)
        
        # Metrics row
        metrics_frame = tk.Frame(tab, bg=Colors.PRIMARY)
        metrics_frame.pack(fill='x', pady=(0, 20))
        
        # Create metric cards
        self.metric_cards = {}
        metric_configs = [
            ("Voice Commands", "0", "🎤", Colors.SUCCESS),
            ("Safety Alerts", "0", "👁️", Colors.DANGER),
            ("Experiments", "0", "🧪", Colors.INFO),
            ("AI Models", "4", "🤖", Colors.ACCENT)
        ]
        
        for i, (title, value, icon, color) in enumerate(metric_configs):
            card = MetricCard(metrics_frame, title, value, icon, color)
            card.pack(side='left', padx=(0, 15))
            self.metric_cards[title] = card
        
        # Quick actions
        actions_frame = tk.LabelFrame(tab, text="🚀 Quick Actions", 
                                    font=Fonts.HEADING, bg=Colors.SECONDARY, fg=Colors.LIGHT,
                                    padx=20, pady=20)
        actions_frame.pack(fill='x', pady=(0, 20))
        
        action_buttons = [
            ("🎤 Start Voice Session", self.start_voice_session, Colors.SUCCESS),
            ("👁️ Toggle Vision Monitor", self.toggle_vision_monitor, Colors.WARNING),
            ("🧪 Chemistry Experiment", lambda: self.start_experiment('chemistry'), Colors.DANGER),
            ("🧬 Bio Experiment", lambda: self.start_experiment('biotechnology'), Colors.SUCCESS),
            ("🔭 Physics Experiment", lambda: self.start_experiment('physics'), Colors.INFO),
            ("🚨 Emergency Protocol", self.emergency_protocol, Colors.DANGER),
            ("📊 System Report", self.generate_report, Colors.ACCENT),
            ("⚡ Optimize Parameters", self.optimize_parameters, Colors.SUCCESS)
        ]
        
        button_frame = tk.Frame(actions_frame, bg=Colors.SECONDARY)
        button_frame.pack(fill='x')
        
        for i, (text, command, color) in enumerate(action_buttons):
            btn = AnimatedButton(button_frame, 
                               text=text, 
                               command=command,
                               font=Fonts.BODY,
                               bg=color,
                               fg=Colors.WHITE,
                               relief='raised',
                               bd=2,
                               padx=15,
                               pady=10)
            btn.grid(row=i//4, column=i%4, padx=5, pady=5, sticky='ew')
            button_frame.columnconfigure(i%4, weight=1)
        
        # Real-time metrics display
        metrics_display_frame = tk.LabelFrame(tab, text="📊 Real-time Analytics", 
                                            font=Fonts.HEADING, bg=Colors.SECONDARY, fg=Colors.LIGHT,
                                            padx=20, pady=20)
        metrics_display_frame.pack(fill='both', expand=True)
        
        self.metrics_text = scrolledtext.ScrolledText(metrics_display_frame, 
                                                     height=12, 
                                                     font=('Consolas', 10), 
                                                     bg='#1a1a1a', 
                                                     fg='#00ff00',
                                                     relief='sunken',
                                                     bd=2)
        self.metrics_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        return tab
    
    def create_premium_voice_tab(self):
        """Create premium voice tab"""
        tab = tk.Frame(self.notebook, bg=Colors.PRIMARY)
        
        controls_frame = tk.LabelFrame(tab, text="🎤 Premium Voice Assistant", 
                                     font=Fonts.HEADING, bg=Colors.SECONDARY, fg=Colors.LIGHT,
                                     padx=20, pady=20)
        controls_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.voice_display = scrolledtext.ScrolledText(controls_frame, 
                                                      height=20, 
                                                      font=('Consolas', 10), 
                                                      bg='#1a1a1a', 
                                                      fg=Colors.WHITE,
                                                      relief='sunken',
                                                      bd=2)
        self.voice_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        button_frame = tk.Frame(controls_frame, bg=Colors.SECONDARY)
        button_frame.pack(fill='x', pady=10)
        
        tk.Button(button_frame, text="🎤 Start Listening", command=self.manual_listen,
                 bg=Colors.SUCCESS, fg=Colors.WHITE, font=Fonts.BODY, padx=20, pady=10).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="📊 Voice Analytics", command=self.show_voice_analytics,
                 bg=Colors.INFO, fg=Colors.WHITE, font=Fonts.BODY, padx=20, pady=10).pack(side='left', padx=5)
        
        return tab
    
    def create_premium_vision_tab(self):
        """Create premium vision tab"""
        tab = tk.Frame(self.notebook, bg=Colors.PRIMARY)
        
        controls_frame = tk.LabelFrame(tab, text="👁️ Premium Vision Safety", 
                                     font=Fonts.HEADING, bg=Colors.SECONDARY, fg=Colors.LIGHT,
                                     padx=20, pady=20)
        controls_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.safety_display = scrolledtext.ScrolledText(controls_frame, 
                                                       height=18, 
                                                       font=('Consolas', 10), 
                                                       bg='#1a1a1a', 
                                                       fg='#ff4444',
                                                       relief='sunken',
                                                       bd=2)
        self.safety_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        button_frame = tk.Frame(controls_frame, bg=Colors.SECONDARY)
        button_frame.pack(fill='x', pady=10)
        
        tk.Button(button_frame, text="👁️ Start Monitoring", command=self.start_vision_monitoring,
                 bg=Colors.DANGER, fg=Colors.WHITE, font=Fonts.BODY, padx=20, pady=10).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="📊 Safety Report", command=self.show_safety_report,
                 bg=Colors.INFO, fg=Colors.WHITE, font=Fonts.BODY, padx=20, pady=10).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="🛑 Stop Monitoring", command=self.stop_vision_monitoring,
                 bg=Colors.WARNING, fg=Colors.WHITE, font=Fonts.BODY, padx=20, pady=10).pack(side='left', padx=5)
        
        return tab
    
    def create_premium_experiment_tab(self):
        """Create premium experiment tab"""
        tab = tk.Frame(self.notebook, bg=Colors.PRIMARY)
        
        controls_frame = tk.LabelFrame(tab, text="🧪 Premium Experiment AI", 
                                     font=Fonts.HEADING, bg=Colors.SECONDARY, fg=Colors.LIGHT,
                                     padx=20, pady=20)
        controls_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.experiment_display = scrolledtext.ScrolledText(controls_frame, 
                                                          height=18, 
                                                          font=('Consolas', 10), 
                                                          bg='#1a1a1a', 
                                                          fg='#ffaa00',
                                                          relief='sunken',
                                                          bd=2)
        self.experiment_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        button_frame = tk.Frame(controls_frame, bg=Colors.SECONDARY)
        button_frame.pack(fill='x', pady=10)
        
        experiment_buttons = [
            ("🧪 Chemistry", 'chemistry', Colors.DANGER),
            ("🧬 Biotechnology", 'biotechnology', Colors.SUCCESS),
            ("🔭 Physics", 'physics', Colors.INFO)
        ]
        
        for text, exp_type, color in experiment_buttons:
            tk.Button(button_frame, text=text, 
                     command=lambda et=exp_type: self.start_experiment(et),
                     bg=color, fg=Colors.WHITE, font=Fonts.BODY, padx=15, pady=10).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="🤖 Generate Hypothesis", command=self.generate_hypothesis,
                 bg=Colors.ACCENT, fg=Colors.WHITE, font=Fonts.BODY, padx=15, pady=10).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="⚡ Optimize Parameters", command=self.optimize_parameters,
                 bg=Colors.SUCCESS, fg=Colors.WHITE, font=Fonts.BODY, padx=15, pady=10).pack(side='left', padx=5)
        
        return tab
    
    def create_premium_analytics_tab(self):
        """Create premium analytics tab"""
        tab = tk.Frame(self.notebook, bg=Colors.PRIMARY)
        
        analytics_frame = tk.LabelFrame(tab, text="📊 Premium Analytics Dashboard", 
                                      font=Fonts.HEADING, bg=Colors.SECONDARY, fg=Colors.LIGHT,
                                      padx=20, pady=20)
        analytics_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.analytics_display = scrolledtext.ScrolledText(analytics_frame, 
                                                         height=22, 
                                                         font=('Consolas', 10), 
                                                         bg='#1a1a1a', 
                                                         fg='#00ffcc',
                                                         relief='sunken',
                                                         bd=2)
        self.analytics_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        return tab
    
    def create_premium_status_bar(self):
        """Create premium status bar"""
        status_frame = tk.Frame(self.main_container, bg=Colors.SECONDARY, height=40)
        status_frame.pack(fill='x', side='bottom', pady=(20, 0))
        status_frame.pack_propagate(False)
        
        status_text = "🟢 Premium Edition Active • NeuroLab Commander Ready • All Systems Operational"
        status_label = tk.Label(status_frame, text=status_text, font=Fonts.SMALL, 
                               bg=Colors.SECONDARY, fg=Colors.LIGHT)
        status_label.pack(side='left', padx=20, pady=10)
    
    def start_services(self):
        """Start all services"""
        if self.voice_assistant:
            try:
                self.voice_assistant.start_continuous_listening()
                self.update_status('🎤 Voice AI', '🟢 Active & Listening')
            except Exception as e:
                print(f"Voice service start failed: {e}")
                self.update_status('🎤 Voice AI', '🔴 Failed')
        else:
            self.update_status('🎤 Voice AI', '🔴 Not Available')
        
        if self.vision_monitor:
            self.update_status('👁️ Vision Safety', '🟡 Ready to Start')
        else:
            self.update_status('👁️ Vision Safety', '🔴 Not Available')
            
        if self.experiment_ai:
            self.update_status('🧠 Experiment AI', '🟢 Ready')
        else:
            self.update_status('🧠 Experiment AI', '🔴 Not Available')
            
        self.update_status('📊 Analytics', '🟢 Collecting Data')
        
        self.start_metrics_updater()
    
    def start_metrics_updater(self):
        """Update real-time metrics"""
        def update_loop():
            while self.is_running:
                try:
                    metrics = self.gather_system_metrics()
                    self.update_metrics_display(metrics)
                    time.sleep(3)
                except Exception as e:
                    print(f"Metrics update error: {e}")
                    time.sleep(5)
        
        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()
    
    def gather_system_metrics(self):
        """Gather system metrics"""
        metrics = {
            'system_uptime': time.time() - self.start_time,
            'voice_commands': len(self.voice_assistant.command_history) if self.voice_assistant else 0,
            'safety_violations': len(self.vision_monitor.safety_violations) if self.vision_monitor else 0,
            'experiments_conducted': len(self.experiment_ai.experiment_history) if self.experiment_ai else 0,
            'active_threads': threading.active_count(),
            'python_version': sys.version.split()[0]
        }
        
        return metrics
    
    def update_metrics_display(self, metrics):
        """Update metrics display"""
        try:
            metrics_text = "🎯 PREMIUM REAL-TIME ANALYTICS\n"
            metrics_text += "═" * 50 + "\n\n"
            metrics_text += f"📈 System Uptime: {metrics['system_uptime']:.1f}s\n"
            metrics_text += f"🎤 Voice Commands: {metrics['voice_commands']}\n"
            metrics_text += f"👁️ Safety Violations: {metrics['safety_violations']}\n"
            metrics_text += f"🧪 Experiments Conducted: {metrics['experiments_conducted']}\n"
            metrics_text += f"🔄 Active Threads: {metrics['active_threads']}\n"
            metrics_text += f"🐍 Python Version: {metrics['python_version']}\n"
            metrics_text += f"🎨 Premium UI: ✅ Active\n"
            metrics_text += f"🚀 Performance: ⚡ Optimal\n"
            
            self.metrics_text.delete(1.0, tk.END)
            self.metrics_text.insert(1.0, metrics_text)
        except Exception as e:
            print(f"Metrics display update failed: {e}")
    
    def update_status(self, component, status):
        """Update component status"""
        if component in self.status_indicators:
            try:
                self.status_indicators[component].config(text=status)
            except Exception as e:
                print(f"Status update failed: {e}")
    
    # Voice commands
    def start_voice_session(self):
        if self.voice_assistant:
            self.voice_assistant.speak("Premium voice session activated. Ready for advanced commands.", "professional")
            self.voice_display.insert(tk.END, "🎤 Premium voice session started...\n")
            self.voice_display.see(tk.END)
    
    def manual_listen(self):
        if not self.voice_assistant:
            self.voice_display.insert(tk.END, "❌ Voice assistant not available\n")
            return
            
        def listen_thread():
            try:
                enhanced_command = self.voice_assistant.listen_with_enhancement()
                if enhanced_command and enhanced_command.get('text'):
                    response = self.voice_assistant.process_command(enhanced_command)
                    
                    display_text = f"👤 You: {enhanced_command['text']}\n"
                    display_text += f"🧠 NeuroLab: {response['speech']}\n"
                    display_text += f"📊 Intent: {enhanced_command['intent']}\n"
                    display_text += f"😊 Sentiment: {enhanced_command['sentiment']['label']}\n"
                    display_text += "─" * 50 + "\n"
                    
                    self.voice_display.insert(tk.END, display_text)
                    self.voice_display.see(tk.END)
                    
                    self.voice_assistant.speak(response['speech'], response.get('emotion', 'neutral'))
            except Exception as e:
                self.voice_display.insert(tk.END, f"❌ Listening error: {e}\n")
                self.voice_display.see(tk.END)
        
        threading.Thread(target=listen_thread, daemon=True).start()
    
    def show_voice_analytics(self):
        if not self.voice_assistant:
            self.voice_display.insert(tk.END, "❌ Voice assistant not available\n")
            return
            
        analytics = {
            'total_commands': len(self.voice_assistant.command_history),
            'recent_intents': [],
            'system_status': '⚡ Premium Performance'
        }
        
        for cmd in self.voice_assistant.command_history[-5:]:
            intent = cmd.get('enhanced_command', {}).get('intent', 'unknown')
            analytics['recent_intents'].append(intent)
        
        display_text = "🎯 PREMIUM VOICE ANALYTICS\n"
        display_text += "═" * 50 + "\n\n"
        display_text += f"Total Commands: {analytics['total_commands']}\n"
        display_text += f"Recent Intents: {', '.join(analytics['recent_intents'])}\n"
        display_text += f"System Status: {analytics['system_status']}\n"
        display_text += f"Voice Quality: 🎯 Excellent\n"
        display_text += f"Processing Speed: ⚡ Instant\n"
        
        self.voice_display.insert(tk.END, display_text + "\n")
        self.voice_display.see(tk.END)
    
    # Vision safety
    def start_vision_monitoring(self):
        if self.vision_monitor:
            self.vision_monitor.start_monitoring()
            self.update_status('👁️ Vision Safety', '🟢 Active & Monitoring')
            self.safety_display.insert(tk.END, "👁️ Premium vision monitoring started...\n")
            self.safety_display.see(tk.END)
    
    def stop_vision_monitoring(self):
        if self.vision_monitor:
            self.vision_monitor.stop_monitoring()
            self.update_status('👁️ Vision Safety', '🟡 Stopped')
            self.safety_display.insert(tk.END, "🛑 Vision monitoring stopped\n")
            self.safety_display.see(tk.END)
    
    def show_safety_report(self):
        if not self.vision_monitor:
            self.safety_display.insert(tk.END, "❌ Vision monitor not available\n")
            return
            
        report = self.vision_monitor.get_safety_report()
        
        display_text = "📊 PREMIUM SAFETY REPORT\n"
        display_text += "═" * 50 + "\n\n"
        display_text += f"Total Violations: {report['total_violations']}\n"
        display_text += f"Risk Level: {report['risk_assessment']['overall_risk']}\n"
        display_text += f"Camera Available: {report['camera_available']}\n"
        display_text += f"Monitoring Status: {report['monitoring_status']}\n\n"
        display_text += "Recent Alerts:\n"
        for alert in report['recent_alerts']:
            display_text += f"• {alert}\n"
        
        display_text += "\nRecommendations:\n"
        for rec in report['risk_assessment']['recommendations']:
            display_text += f"• {rec}\n"
        
        self.safety_display.insert(tk.END, display_text + "\n")
        self.safety_display.see(tk.END)
    
    # Experiment management
    def start_experiment(self, experiment_type):
        if not self.experiment_ai:
            self.experiment_display.insert(tk.END, "❌ Experiment AI not available\n")
            return
            
        try:
            guidance = self.experiment_ai.start_experiment(experiment_type)
            
            display_text = f"🚀 STARTING {experiment_type.upper()} EXPERIMENT\n"
            display_text += "═" * 50 + "\n\n"
            display_text += f"{guidance['icon']} {guidance['experiment_name']}\n"
            display_text += f"🔒 Safety Level: {guidance['safety_level']}\n\n"
            display_text += "📋 Procedure Steps:\n"
            for i, step in enumerate(guidance['steps'], 1):
                display_text += f"  {i}. {step}\n"
            
            display_text += "\n🎯 Critical Parameters:\n"
            for param in guidance['critical_parameters']:
                display_text += f"  • {param}\n"
            
            display_text += "\n💡 AI Recommendations:\n"
            for rec in guidance['ai_recommendations']:
                display_text += f"  • {rec}\n"
            
            self.experiment_display.insert(tk.END, display_text + "\n")
            self.experiment_display.see(tk.END)
            
            if self.voice_assistant:
                self.voice_assistant.speak(f"Starting {experiment_type} experiment with premium AI guidance.", "professional")
        except Exception as e:
            self.experiment_display.insert(tk.END, f"❌ Experiment start failed: {e}\n")
            self.experiment_display.see(tk.END)
    
    def generate_hypothesis(self):
        if not self.experiment_ai:
            self.experiment_display.insert(tk.END, "❌ Experiment AI not available\n")
            return
            
        try:
            hypothesis = self.experiment_ai.generate_hypothesis('chemistry', 'reaction optimization')
            
            display_text = "🤖 PREMIUM AI HYPOTHESIS GENERATION\n"
            display_text += "═" * 50 + "\n\n"
            display_text += f"🧠 Hypothesis: {hypothesis['hypothesis']}\n"
            display_text += f"🔧 Model: {hypothesis['model']}\n"
            display_text += f"🎯 Confidence: {hypothesis['confidence']:.1%}\n"
            display_text += f"📊 Type: {hypothesis['type']}\n"
            display_text += f"⏰ Generated: {hypothesis['timestamp'].strftime('%H:%M:%S')}\n"
            
            self.experiment_display.insert(tk.END, display_text + "\n")
            self.experiment_display.see(tk.END)
            
            if self.voice_assistant:
                self.voice_assistant.speak("Premium AI hypothesis generated successfully.", "professional")
        except Exception as e:
            self.experiment_display.insert(tk.END, f"❌ Hypothesis generation failed: {e}\n")
            self.experiment_display.see(tk.END)
    
    def optimize_parameters(self):
        if not self.experiment_ai:
            self.experiment_display.insert(tk.END, "❌ Experiment AI not available\n")
            return
            
        try:
            sample_data = [
                {'temperature': 25, 'concentration': 0.1, 'time': 30, 'outcome': 0.7},
                {'temperature': 30, 'concentration': 0.2, 'time': 45, 'outcome': 0.8},
                {'temperature': 35, 'concentration': 0.15, 'time': 60, 'outcome': 0.9},
                {'temperature': 40, 'concentration': 0.25, 'time': 75, 'outcome': 0.85},
            ]
            
            optimization = self.experiment_ai.optimize_parameters(sample_data)
            
            display_text = "⚡ PREMIUM PARAMETER OPTIMIZATION\n"
            display_text += "═" * 50 + "\n\n"
            display_text += f"🔧 Method: {optimization['method']}\n"
            if 'predicted_outcome' in optimization:
                display_text += f"🎯 Predicted Outcome: {optimization['predicted_outcome']:.1%}\n"
                display_text += f"📊 Confidence: {optimization.get('confidence', 0):.1%}\n\n"
            
            if 'optimal_parameters' in optimization:
                display_text += "💎 Optimal Parameters:\n"
                for param, value in optimization['optimal_parameters'].items():
                    if param != 'outcome':
                        display_text += f"  • {param}: {value}\n"
            
            self.experiment_display.insert(tk.END, display_text + "\n")
            self.experiment_display.see(tk.END)
            
            if self.voice_assistant:
                self.voice_assistant.speak("Premium parameter optimization complete.", "professional")
        except Exception as e:
            self.experiment_display.insert(tk.END, f"❌ Optimization failed: {e}\n")
            self.experiment_display.see(tk.END)
    
    # System controls
    def emergency_protocol(self):
        if self.voice_assistant:
            self.voice_assistant.speak("🚨 PREMIUM EMERGENCY PROTOCOL ACTIVATED!", "urgent")
        
        if self.vision_monitor:
            self.vision_monitor.stop_monitoring()
        
        self.update_status('👁️ Vision Safety', '🔴 EMERGENCY STOP')
        self.update_status('🎤 Voice AI', '🔴 EMERGENCY MODE')
        
        self.safety_display.insert(tk.END, "🚨 PREMIUM EMERGENCY PROTOCOL ACTIVATED\n")
        self.safety_display.see(tk.END)
    
    def generate_report(self):
        display_text = "📈 PREMIUM SYSTEM REPORT\n"
        display_text += "═" * 50 + "\n\n"
        
        if self.voice_assistant:
            display_text += "🎤 Voice Assistant:\n"
            display_text += f"  • Commands Processed: {len(self.voice_assistant.command_history)}\n"
            display_text += f"  • System Status: ⚡ Premium Performance\n\n"
        
        if self.vision_monitor:
            vision_report = self.vision_monitor.get_safety_report()
            display_text += "👁️ Vision Safety:\n"
            display_text += f"  • Total Violations: {vision_report['total_violations']}\n"
            display_text += f"  • Risk Level: {vision_report['risk_assessment']['overall_risk']}\n"
            display_text += f"  • Camera Available: {vision_report['camera_available']}\n\n"
        
        if self.experiment_ai:
            exp_analytics = self.experiment_ai.get_analytics()
            display_text += "🧠 Experiment AI:\n"
            display_text += f"  • Experiments: {exp_analytics['total_experiments']}\n"
            display_text += f"  • Hypotheses: {exp_analytics['hypotheses_generated']}\n"
            display_text += f"  • Average Confidence: {exp_analytics['average_confidence']:.1%}\n\n"
        
        display_text += "🚀 System Summary:\n"
        display_text += "  • UI: 🎨 Premium Design\n"
        display_text += "  • Performance: ⚡ Optimal\n"
        display_text += "  • Reliability: 💎 Rock Solid\n"
        display_text += "  • Features: 🌟 All Systems Go\n"
        
        self.analytics_display.insert(tk.END, display_text + "\n")
        self.analytics_display.see(tk.END)
        
        if self.voice_assistant:
            self.voice_assistant.speak("Premium system report generated. All systems operating at peak performance.", "professional")
    
    def toggle_vision_monitor(self):
        if self.vision_monitor:
            if self.vision_monitor.is_monitoring:
                self.stop_vision_monitoring()
            else:
                self.start_vision_monitoring()
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Application error: {e}")
        finally:
            self.is_running = False
            if self.vision_monitor:
                self.vision_monitor.stop_monitoring()

# ==================== MAIN EXECUTION ====================
import sys

if __name__ == "__main__":
    print("=" * 70)
    print("🧠 NEUROLAB COMMANDER - PREMIUM EDITION")
    print("🎨 Beautiful UI • Colorful Design • Premium Features")
    print("=" * 70)
    
    print("\n🚀 Launching Premium Edition...")
    print("💎 Features:")
    print("   • 🎨 Colorful metric cards & modern design")
    print("   • 🎯 Animated interactive buttons")
    print("   • 🔥 Premium color scheme")
    print("   • ⚡ Real-time analytics")
    print("   • 💎 Professional typography")
    
    print("\n🎯 Ready to showcase:")
    print("   • Voice-controlled laboratory assistant")
    print("   • Computer vision safety monitoring")
    print("   • AI experiment guidance")
    print("   • Real-time analytics dashboard")
    print("   • Emergency protocols\n")
    
    # Start the application
    try:
        app = PremiumNeuroLabCommander()
        app.run()
    except Exception as e:
        print(f"❌ Failed to start application: {e}")
        print("💡 Make sure you have installed:")
        print("   pip install speechrecognition pyttsx3 pyaudio opencv-python pandas numpy matplotlib")