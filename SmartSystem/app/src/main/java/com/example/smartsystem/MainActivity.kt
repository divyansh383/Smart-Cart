package com.example.smartsystem

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import android.content.Intent
import android.view.View
import android.widget.Button


class MainActivity : AppCompatActivity() {

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        setContentView(R.layout.activity_main)
        val tvsignup = findViewById<TextView>(R.id.tvSignUp)
        val tvsignupsecond = findViewById<TextView>(R.id.tvSignUpSecond)

        tvsignup.setOnClickListener(onClickSignUp())
        tvsignupsecond.setOnClickListener(onClickSignUp())

        findViewById<Button>(R.id.loginButton).setOnClickListener(){
            val intent = Intent(this,user::class.java)
            startActivity(intent)
        }

        }
    private fun onClickSignUp(): View.OnClickListener {
        return View.OnClickListener {
            val intent = Intent(this, RegisterActivity::class.java)
            startActivity(intent)
        }
        
    }
}