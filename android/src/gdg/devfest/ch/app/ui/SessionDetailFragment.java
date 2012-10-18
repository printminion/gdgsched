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

package gdg.devfest.ch.app.ui;


/**
 * A fragment that shows detail information for a session, including session title, abstract,
 * time information, speaker photos and bios, etc.
 *
 * <p>This fragment is used in a number of activities, including
 * {@link com.google.android.apps.iosched.ui.phone.SessionDetailActivity},
 * {@link com.google.android.apps.iosched.ui.tablet.SessionsVendorsMultiPaneActivity},
 * {@link com.google.android.apps.iosched.ui.tablet.MapMultiPaneActivity}, etc.
 */
public class SessionDetailFragment extends com.google.android.apps.iosched.ui.SessionDetailFragment {

    // Set this boolean extra to true to show a variable height header
    public static final String EXTRA_VARIABLE_HEIGHT_HEADER =
            "com.google.android.iosched.extra.VARIABLE_HEIGHT_HEADER";

}
