
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:my_app/widgets/login_screen/email_field.dart';
import 'package:my_app/widgets/login_screen/password_field.dart';
import 'package:my_app/widgets/login_screen/login_button.dart';
import 'package:my_app/widgets/login_screen/google_sign_in_button.dart';
import 'register_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Фон на весь экран
          Positioned.fill(
            child: Image.asset(
              "assets/images/login_bg.jpg",
              fit: BoxFit.cover, // растягивает под экран
            ),
          ),

          // Поля + кнопки
          Center(
            child: SingleChildScrollView(
              child: Container(
                padding: const EdgeInsets.all(24),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.85),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Image.asset("assets/images/logo.png", height: 80),
                    const SizedBox(height: 20),
                    EmailField(controller: emailController),
                    const SizedBox(height: 16),
                    PasswordField(controller: passwordController),
                    const SizedBox(height: 16),
                    LoginButton(onPressed: _loginWithEmail),
                    const SizedBox(height: 12),
                    GoogleSignInButton(onPressed: _loginWithGoogle),
                    const SizedBox(height: 16),
                    TextButton(
                      onPressed: () => Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => const RegisterScreen()),
                      ),
                      child: const Text("Create an account"),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Future<void> _loginWithEmail() async {
    try {
      await FirebaseAuth.instance.signInWithEmailAndPassword(
        email: emailController.text.trim(),
        password: passwordController.text.trim(),
      );
    } on FirebaseAuthException catch (e) {
      ScaffoldMessenger.of(context)
          .showSnackBar(SnackBar(content: Text(e.message ?? 'Login failed')));
    }
  }

  Future<void> _loginWithGoogle() async {
    // Логика Google Sign-In
  }
}
