
import 'package:flutter/material.dart';
import 'api_client.dart';

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final api = ApiClient();
  List<Map<String, dynamic>> notes = [];
  bool loading = true;

  @override
  void initState() {
    super.initState();
    _loadNotes();
  }

  Future<void> _loadNotes() async {
    await api.login('Admin', 'star4536446'); // для теста
    notes = await api.getNotes();
    setState(() => loading = false);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('ProLearner Notes')),
        body: loading
            ? const Center(child: CircularProgressIndicator())
            : ListView.builder(
                itemCount: notes.length,
                itemBuilder: (_, i) => ListTile(
                  title: Text(notes[i]['title']),
                  subtitle: Text(notes[i]['body'] ?? ''),
                ),
              ),
      ),
    );
  }
}

