package com.example.smartsystem

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.SurfaceHolder
import android.widget.Button
import android.widget.Toast
import com.example.smartsystem.databinding.ActivityQrcodescanBinding
import com.example.smartsystem.databinding.ActivityUserBinding
import com.google.android.gms.vision.CameraSource
import com.google.android.gms.vision.Detector
import com.google.android.gms.vision.barcode.Barcode
import com.google.android.gms.vision.barcode.BarcodeDetector
import java.io.IOException

class qrcodescan : AppCompatActivity() {
    private lateinit var binding: ActivityQrcodescanBinding
    private lateinit var barcodeDetector: BarcodeDetector
    private lateinit var cameraSource: CameraSource
    var intentData = ""
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_qrcodescan)
        binding = ActivityQrcodescanBinding.inflate(layoutInflater)
        setContentView(binding.root)
    }
    private fun iniBc(){
        barcodeDetector = BarcodeDetector.Builder(this).setBarcodeFormats(Barcode.ALL_FORMATS).build()
        cameraSource = CameraSource.Builder(this,barcodeDetector).setRequestedPreviewSize(1920,1080).setAutoFocusEnabled(true)
        //    .setFacing(CameraSource.CAMERA_FACING_FRONT)
            .build()
        binding.surfaceView!!.holder.addCallback(object : SurfaceHolder.Callback{
            @SuppressLint("MissingPermission")
            override fun surfaceCreated(p0: SurfaceHolder) {
                try{
                    cameraSource.start(binding.surfaceView!!.holder)
                }catch (e:IOException){
                    e.printStackTrace()
                }
            }

            override fun surfaceChanged(p0: SurfaceHolder, p1: Int, p2: Int, p3: Int) {

            }

            override fun surfaceDestroyed(p0: SurfaceHolder) {
                cameraSource.stop()
            }

        })
        barcodeDetector.setProcessor(object :Detector.Processor<Barcode>{
            override fun release() {
                Toast.makeText(applicationContext, "barcode scanner has been stopped",Toast.LENGTH_SHORT).show()
            }

            override fun receiveDetections(detections: Detector.Detections<Barcode>) {
                val barcode = detections.detectedItems
                if(barcode.size() != 0){
                    binding.txtBarcodevalue!!.post{
                        binding.btnAction!!.text = "SEARCH ITEM"
                        intentData = barcode.valueAt(0).displayValue
                        binding.txtBarcodevalue.setText(intentData)
                        finish()
                    }
                }
            }

        })
    }
    override fun onPause(){
        super.onPause()
        cameraSource!!.release()
    }
    override fun onResume(){
        super.onResume()
        iniBc()
    }
}