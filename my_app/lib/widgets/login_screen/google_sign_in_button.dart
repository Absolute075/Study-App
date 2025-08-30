import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:google_sign_in/google_sign_in.dart';

class GoogleSignInButton extends StatelessWidget {
  const GoogleSignInButton({super.key});

  Future<void> signInWithGoogle() async {
    try {
      // Шаг 1: Вход через Google
      final GoogleSignInAccount? googleUser = await GoogleSignIn().signIn();
      if (googleUser == null) return; // пользователь отменил вход

      // Шаг 2: Получаем аутентификацию Google
      final GoogleSignInAuthentication googleAuth = await googleUser.authentication;

      // Шаг 3: Создаем credential для Firebase
      final credential = GoogleAuthProvider.credential(
        accessToken: googleAuth.accessToken,
        idToken: googleAuth.idToken,
      );

      // Шаг 4: Входим в Firebase
      await FirebaseAuth.instance.signInWithCredential(credential);
      print("Успешный вход через Google!");
    } catch (e) {
      print("Ошибка при Google Sign-In: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: OutlinedButton.icon(
        onPressed: signInWithGoogle,
        icon: Image.network(
          "https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg",
          width: 20,
          height: 20,
        ),
        label: const Text(
          "Sign in with Google",
          style: TextStyle(color: Colors.black87),
        ),
        style: OutlinedButton.styleFrom(
          padding: const EdgeInsets.symmetric(vertical: 14),
          side: const BorderSide(color: Colors.grey),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
    );
  }
}
