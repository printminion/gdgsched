package gdg.devfest.ch.app.ui.tablet;

import android.annotation.TargetApi;
import android.os.Build;

/**
 * A multi-pane activity, consisting of a {@link TracksDropdownFragment}
 * (top-left), a {@link SessionsFragment} or {@link VendorsFragment}
 * (bottom-left), and a {@link SessionDetailFragment} or
 * {@link VendorDetailFragment} (right pane).
 */
@TargetApi(Build.VERSION_CODES.HONEYCOMB)
public class SessionsVendorsMultiPaneActivity
		extends
		com.google.android.apps.iosched.ui.tablet.SessionsVendorsMultiPaneActivity {
}