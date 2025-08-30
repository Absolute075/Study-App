import 'package:flutter/material.dart';

class GoogleSignInButton extends StatelessWidget {
  final VoidCallback onPressed;
  const GoogleSignInButton({super.key, required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton.icon(
      icon: Image.asset("assets/images/google_icon.png", height: 24),
      label: const Text("Sign in with Google"),
      onPressed: onPressed,
    );
  }
}
