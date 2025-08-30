import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../widgets/register_screen/email_field.dart';
import '../widgets/register_screen/password_field.dart';
import '../widgets/register_screen/username.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _usernameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  Future<void> registerUser(BuildContext context, String username, String email, String password) async {
    final response = await http.post(
      Uri.parse("https://study-app-a53x.onrender.com/api/register/"),
      headers: {"Content-Type": "application/json"},
      body: json.encode({
        "username": username,
        "email": email,
        "password": password,
      }),
    );

    if (response.statusCode == 200 || response.statusCode == 201) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Регистрация успешна ✅")),
      );
      Navigator.pop(context);
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Ошибка: ${response.body}")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Sign Up")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            UsernameField(controller: _usernameController),
            const SizedBox(height: 12),
            EmailField(controller: _emailController),
            const SizedBox(height: 12),
            PasswordField(controller: _passwordController),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () async {
                await registerUser(context, _usernameController.text, _emailController.text, _passwordController.text);
              },
              child: const Text("Sign Up"),
            ), // Added comma and closing parenthesis
          ],
        ),
      ),
    );
  }
} // Added closing curly braces