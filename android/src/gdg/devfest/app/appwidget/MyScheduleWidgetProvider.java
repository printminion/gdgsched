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

package gdg.devfest.app.appwidget;

import gdg.devfest.ISetup;
import android.annotation.TargetApi;
import android.os.Build;

/**
 * The app widget's AppWidgetProvider.
 */
@TargetApi(Build.VERSION_CODES.HONEYCOMB)
public class MyScheduleWidgetProvider extends
		com.google.android.apps.iosched.appwidget.MyScheduleWidgetProvider {

	public static final String CLICK_ACTION = ISetup.EVENT_PACKAGE_NAME
			+ ".appwidget.action.CLICK";
	public static final String REFRESH_ACTION = ISetup.EVENT_PACKAGE_NAME
			+ ".appwidget.action.REFRESH";
	public static final String EXTRA_PERFORM_SYNC = ISetup.EVENT_PACKAGE_NAME
			+ ".appwidget.extra.PERFORM_SYNC";

}
