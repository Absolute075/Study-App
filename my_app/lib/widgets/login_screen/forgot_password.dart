import 'package:flutter/material.dart';

class ForgotPasswordText extends StatelessWidget {
  const ForgotPasswordText({super.key});

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.centerRight,
      child: TextButton(
        onPressed: () {
          // TODO: Add forgot password logic
        },
        child: const Text(
          "Forgot password?",
          style: TextStyle(color: Colors.indigo),
        ),
      ),
    );
  }
}
