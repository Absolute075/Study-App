import 'package:flutter/material.dart';

class SignupRedirect extends StatelessWidget {
  const SignupRedirect({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const Text("Don't have an account?"),
        TextButton(
          onPressed: () {
            // TODO: navigate to signup screen
          },
          child: const Text("Sign Up"),
        ),
      ],
    );
  }
}
