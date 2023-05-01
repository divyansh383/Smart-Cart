package com.example.smartsystem

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import org.w3c.dom.Text

class RegisterActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)
        val tvlogin = findViewById<TextView>(R.id.tvLogin)
        tvlogin.setOnClickListener {
            finish()
        }
    }
}