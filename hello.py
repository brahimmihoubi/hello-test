import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
            seedColor: const Color.fromARGB(255, 21, 97, 211)),
        useMaterial3: true,
      ),
      home: const Welcomepage(),
    );
  }
}

class Welcomepage extends StatefulWidget {
  const Welcomepage({super.key});

  @override
  State<Welcomepage> createState() => _WelcomepageState();
}

class _WelcomepageState extends State<Welcomepage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Welcome'),
          centerTitle: true,
          backgroundColor: Colors.blueAccent,
        ),
        body: SingleChildScrollView(
          child: Center(
              child: Column(
            children: [
              const SizedBox(height: 30.0),
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blueAccent,
                ),
                onPressed: () {},
                child: const Text('Click'),
              ),
              const SizedBox(height: 30.0),
              Image.asset('images/urban-welcome.png'),
              Column(
                children: List.generate(
                  2,
                  (index) => Image.asset('images/flutter-welcome.png'),
                ),
              ),
              Image.asset(
                  'images/urban-butler-and-hostess-welcoming-into-hotel-1.png'),
              Column(
                children: List.generate(
                  3,
                  (index) => Image.asset('images/flutter-welcome.png'),
                ),
              ),
              Image.asset('images/urban-vegan-cafe-staff-welcoming.png'),
              Column(
                children: List.generate(
                  4,
                  (index) => Image.asset('images/flutter-welcome.png'),
                ),
              )
            ],
          )),
        ));
  }
}
 
