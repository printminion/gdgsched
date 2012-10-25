package de.gdg.devfest.ka.app.ui.tablet;

import android.annotation.TargetApi;
import android.os.Build;

/**
 * A multi-pane activity, where the full-screen content is a {@link MapFragment}
 * and popup content may be visible at any given time, containing either a
 * {@link SessionsFragment} (representing sessions for a given room) or a
 * {@link SessionDetailFragment}.
 */
@TargetApi(Build.VERSION_CODES.HONEYCOMB)
public class MapMultiPaneActivity extends
		com.google.android.apps.iosched.ui.tablet.MapMultiPaneActivity {
}
