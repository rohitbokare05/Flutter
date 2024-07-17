import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:stadium_app/constants/api.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String _message = 'Fetching data...';

  // void fetchData() async {
  //   try {
  //     http.Response response = await http.get(Uri.parse(api));
  //     // var data = response.body;
  //     // data = json.decode(data);
  //     // print(data);
  //     print(response.body);
  //   } catch (e) {
  //     print("Error is $e ");
  //   }
  // }
  Future<void> fetchData() async {
    final response = await http.get(Uri.parse('http://10.81.2.13:8000/'));

    if (response.statusCode == 200) {
      setState(() {
        _message = json.decode(response.body)['message'];
      });
    } else {
      setState(() {
        _message = 'Failed to load data';
      });
    }
  }

  @override
  void initState() {
    fetchData();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Flutter Django example"),
      ),
      body: Center(
        child: Text(_message),
      ),
    );
  }
}
