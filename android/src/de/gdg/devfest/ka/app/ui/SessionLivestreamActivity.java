package de.gdg.devfest.ka.app.ui;


import android.annotation.TargetApi;
import android.os.Build;
/**
 * An activity that displays the session live stream video which is pulled in
 * from YouTube. The UI adapts for both phone and tablet. As we want to prevent
 * the YouTube player from restarting and buffering again on orientation change,
 * we handle configuration changes manually.
 */
@TargetApi(Build.VERSION_CODES.HONEYCOMB)
public class SessionLivestreamActivity extends
		com.google.android.apps.iosched.ui.SessionLivestreamActivity {
}