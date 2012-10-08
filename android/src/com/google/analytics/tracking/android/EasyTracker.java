/*
 * Copyright 2012 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.analytics.tracking.android;

import com.google.android.apps.analytics.GoogleAnalyticsTracker;
import com.google.android.apps.iosched.Config;

import android.app.Activity;
import android.content.Context;
import android.util.Log;

/**
 * Temporarily just a stub.
 */
public class EasyTracker {
	
	private GoogleAnalyticsTracker tracker;
	
	String TAG = "EasyTracker";
	
    public static EasyTracker getTracker() {
        return new EasyTracker();
    }
    
    private EasyTracker() {
    	Log.d(TAG, "EasyTracker");
    	tracker = GoogleAnalyticsTracker.getInstance();
        
    }

    public void trackView(String s) {
    	Log.d(TAG, "trackView");
    	tracker.trackPageView(s);
    }

    public void trackActivityStart(Activity activity) {
    	Log.d(TAG, "trackActivityStart:" + activity.getLocalClassName());
    	tracker.trackPageView(activity.getLocalClassName());
    }

    public void trackActivityStop(Activity activity) {
    	Log.d(TAG, "trackActivityStop");
    	tracker.stopSession();
    }

    public void setContext(Context context) {
    	Log.d(TAG, "setContext");
    	tracker.startNewSession(Config.GOOGLE_ANALYTICS, 1, context.getApplicationContext());
    }

    public void trackEvent(String s1, String s2, String s3, long l) {
    	Log.d(TAG, "trackEvent");
    	tracker.trackEvent(s1, s2, s3, 0);
    }

    public void dispatch() {
    	Log.e(TAG, "dispatch");
    	tracker.dispatch();
    }
}
