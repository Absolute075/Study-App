plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android") // Kotlin support
    id("com.google.gms.google-services") // Firebase
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.prolearner.app.prolearner_study_app"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = flutter.ndkVersion

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    kotlinOptions {
        jvmTarget = "11"
    }

    defaultConfig {
        applicationId = "com.prolearner.app.prolearner_study_app" // ⚠️ Должно совпадать с google-services.json
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

flutter {
    source = "../.."
}
