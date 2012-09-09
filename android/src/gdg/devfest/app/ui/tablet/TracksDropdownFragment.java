package gdg.devfest.app.ui.tablet;

import android.annotation.TargetApi;
import android.os.Build;

/**
 * A tablet-specific fragment that emulates a giant
 * {@link android.widget.Spinner}-like widget. When touched, it shows a
 * {@link ListPopupWindow} containing a list of tracks, using
 * {@link TracksAdapter}. Requires API level 11 or later since
 * {@link ListPopupWindow} is API level 11+.
 */
@TargetApi(Build.VERSION_CODES.HONEYCOMB)
public class TracksDropdownFragment extends
		com.google.android.apps.iosched.ui.tablet.TracksDropdownFragment {
}