
import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class ApiClient {
  final _dio = Dio(BaseOptions(baseUrl: 'https://study-app-a53x.onrender.com/api/'));
  final _storage = const FlutterSecureStorage();

  ApiClient() {
    _dio.interceptors.add(InterceptorsWrapper(
      onRequest: (options, handler) async {
        final token = await _storage.read(key: 'access');
        if (token != null) {
          options.headers['Authorization'] = 'Bearer $token';
        }
        handler.next(options);
      },
    ));
  }

  Future<void> login(String username, String password) async {
    final r = await _dio.post('/token/', data: {
      'username': username,
      'password': password,
    });
    await _storage.write(key: 'access', value: r.data['access']);
    await _storage.write(key: 'refresh', value: r.data['refresh']);
  }

  Future<List<Map<String, dynamic>>> getNotes() async {
    final r = await _dio.get('/notes/');
    return (r.data as List).cast<Map<String, dynamic>>();
  }
}
